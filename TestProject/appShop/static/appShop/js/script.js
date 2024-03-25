let addBack = document.querySelectorAll("#addback")
addBack.forEach((btn) => {
    btn.addEventListener('click', () => {
        let elements = btn.closest('.card')
        let title = elements.querySelector('h1').textContent
        let product_id = btn.getAttribute('data-product-id')

        let back = document.querySelector('.back')
        let content = document.createElement('div')
        content.innerHTML = `<p>${title}</p><button onclick="RBack(this);" id="removebacked" data-product-id="${product_id}">Удалить</button>`
        back.appendChild(content)

        $.ajax({
            type: 'POST',
            data: {
                id: product_id,
                type: 'add',
                csrfmiddlewaretoken: document.querySelector('meta[name="csrf-token"]').getAttribute('content')
            }
        })
    })
})

function RBack(event){
    let product_id = event.getAttribute('data-product-id');
    document.querySelector('.back').removeChild(event.closest('div'))
    $.ajax({
        type: 'POST',
        data: {
            id: product_id,
            type: 'remove',
            csrfmiddlewaretoken: document.querySelector('meta[name="csrf-token"]').getAttribute('content')
        }
    })
}

document.querySelector("#FormAjax").addEventListener('submit', (e)=>{
    e.preventDefault();
    let form = e.target
    let text = form.querySelector('textarea[name="desc"]').value
    let csrf_token = form.querySelector('input[name="csrfmiddlewaretoken"]').value
    $.ajax({
        type: "POST",
        url: form.getAttribute('action'),
        data: {
            csrfmiddlewaretoken: csrf_token,
            texteria: text 
        },
        success: function (response) {
            console.log(response)
            // location.href = "/"
        }
    })
})