document.addEventListener("DOMContentLoaded", function (){
    document.querySelector("#id_title").addEventListener('input', function (){
        let title = document.querySelector("#id_title").value.replace(/ /g, '-')
        document.querySelector("#id_name_url").value = title 
    })
})
