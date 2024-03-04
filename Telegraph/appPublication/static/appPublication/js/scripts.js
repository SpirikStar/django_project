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
            success: function (response){},
            error: function (response){}
        })
    })
})