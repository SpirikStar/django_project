tinymce.init({
    selector: '#EditContent',
    height: 500,
    plugins: [
        'advlist', 'autolink',
        'lists', 'link', 'image', 'charmap', 'preview', 'anchor', 'searchreplace', 'visualblocks',
        'fullscreen', 'insertdatetime', 'media', 'table', 'help', 'wordcount'
    ],
    toolbar: 'undo redo | formatpainter casechange blocks | bold italic backcolor | ' +
        'alignleft aligncenter alignright alignjustify | ' +
        'bullist numlist checklist outdent indent | removeformat | a11ycheck code table help'
});


$(document).ready(function (){
    $("#FormContent").submit(function (e){
        e.preventDefault();
        let form = $(this)
        $.ajax({
            type: "POST",
            data:{
                csrfmiddlewaretoken: form.find('input[name="csrfmiddlewaretoken"]').val(),
                content: form.find('textarea[name="content"]').val()
            },
            success: function (response){
                if (response.status == 'ok') {
                    // let div = document.querySelector('.story-links')
                    // let a = document.createElement('a')
                    // a.textContent = `Перейдите по ссылке: ${response.url}`
                    // a.href = response.url
                    // div.appendChild(a)

                    let div = $('.story-links')
                    let content = $(`
                    <p>
                        <a href="${response.url}">Перейдите по ссылке: ${response.url}</a>
                    </p>
                    `)
                    div.append(content)
                } else{
                    alert("Ссылка на публикацию не доступна, повторите позже")
                }
            },
            error: function (response){}
        })
    })
})