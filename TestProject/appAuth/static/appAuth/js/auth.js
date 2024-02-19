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
})