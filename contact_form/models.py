from django.db import models


class ContactFormModel(models.Model):
    """Контактная форма"""
    username = models.CharField('Пользователь', max_length=20)
    email = models.EmailField('Почта')
    text = models.TextField('Текст', max_length=200)
    date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'КонтактФорма'
        verbose_name_plural = 'КонтактФормы'

    def __str__(self):
        return self.username

