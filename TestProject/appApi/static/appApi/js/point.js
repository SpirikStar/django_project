$(document).ready(function () {
    $('.send-btn').click(function () {
        $.ajax({
            type: 'POST',
            url: '/api',
            data: {
                len_password:$('#len_password').val(),
                count_password:$('#count_password').val(),
                csrfmiddlewaretoken: $('meta[name="csrf-token"]').attr("content")
            },
            success: function (response){
                for (let i = 0; i < response.data_password.length; i++){
                    let section = document.querySelector('#passwords')
                    let p = document.createElement('p')
                    p.textContent = response.data_password[i]
                    section.appendChild(p)
                }
            },
            error: function(response){}             
        })
    })
})