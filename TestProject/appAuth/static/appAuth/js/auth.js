$(document).ready(function (){
    $('#FormAuth').submit(function (e) {
        e.preventDefault();
        let form = $(this)
        let csrfmiddlewaretoken = form.find('input[name="csrfmiddlewaretoken"]').val();
        let login = form.find('input[name="login"]').val()
        let password = form.find('input[name="password"]').val()
        
        $.ajax({
            type: "POST",
            url: "/auth",
            data: {
                "csrfmiddlewaretoken": csrfmiddlewaretoken,
                "login": login,
                "password": password,
            },
            success: function (response){
                console.log(response)
            }
        })

    })
    $('#FormReg').submit(function (e){
        e.preventDefault();
        let form = $(this)
        let first_name = form.find("input[name='first_name']").val()
        let last_name = form.find("input[name='last_name']").val()
        let email = form.find("input[name='email']").val()
        let login = form.find("input[name='login']").val()
        let password_one = form.find("input[name='password_one']").val()
        let password_two = form.find("input[name='password_two']").val()
        let csrfmiddlewaretoken = form.find('input[name="csrfmiddlewaretoken"]').val();

        if (password_one == password_two){
            $.ajax({
                type: "POST",
                url: "/auth/reg",
                data: {
                    csrfmiddlewaretoken: csrfmiddlewaretoken,
                    first_name: first_name,
                    last_name: last_name,
                    email: email,
                    login: login,
                    password_one: password_one,
                },
                success: function (response) {
                    if (response.status == 'ok'){
                        $('#result').text("Регистрация прошла успешно!")
                    } else if (response.status == 'NoLogin') {
                        $('#result').text("Регистрация не прошла! Неверный логин")
                    } else {
                        $('#result').text("Упсс...Что-то пошло не так!")
                    }
                }
            })
        } else {
            $('#result').text("Пароль не совпадают")
        }
    })
})