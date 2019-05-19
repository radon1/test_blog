// Установка csrf_token
(function () {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
})();

// обработать форму отправки комментария.
$(".form-add-comment").submit(function (e) {
    e.preventDefault();
    // var url = $(this).attr('action');
    // var data = $(this).serialize();
    // $.post(
    //     url,
    //     data,
    //     function (response) {
    //         window.location = response.location;
    //     },
    // );
     $.ajax({
            url: $(this).attr('action'),
            type: "POST",
            data: $(this).serialize(),
            success: (response) => {
                alert("Комментарий успешно отправлен");
                $("#id_text").val('');
            },
            error: (response) => {
                alert("Ошибка отправки комментария")
            }
        })
});
