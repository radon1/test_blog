from django.test import TestCase, Client

from .models import Category, Post


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        cat = Category.objects.create(name="Test", slug="test")
        Post.objects.create(
            category=cat,
            title="Product-test",
            text="Desc",
            slug="product-test")

    def test_category(self):
        category = Category.objects.get(slug="test")
        self.assertEqual(category.name, "Test")

    def test_category_exists(self):
        category = Category.objects.filter(slug="test")
        self.assertTrue(category.exists())

    def test_my(self):
        product = Post.objects.get(category__name__icontains="Test")
        self.assertEqual(product.title, 'Product-test')

    def test_details(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_details2(self):
        response = self.client.get('/lalala/')
        #print(response.context)
        self.assertEqual(response.status_code, 200)

    def test_cat_get(self):
        response = self.client.get('/test/product-test/')
        self.assertEqual(response.status_code, 200)
        print(response.context["new"].created)

    def test_cat_get2(self):
        response = self.client.get('/test/product-test/')
        self.assertEqual(response.context["new"].text, "Desc")
