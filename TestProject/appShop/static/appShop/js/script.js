let addBack = document.querySelectorAll("#addback")
// addBack.forEach(function (){})
addBack.forEach((btn) => {
    btn.addEventListener('click', () => {
        let elements = btn.closest('.card')
        let title = elements.querySelector('h1').textContent
        let product_id = btn.getAttribute('data-product-id')

        let back = document.querySelector('.back')
        let content = document.createElement('div')
        content.innerHTML = `<p>${title}</p><button data-product-id="${product_id}">Удалить</button>`
        back.appendChild(content)

        $.ajax({
            type: 'POST',
            data: {
                id: product_id,
                csrfmiddlewaretoken: document.querySelector('meta[name="csrf-token"]').getAttribute('content')
            }
        })
    })
})