let section = document.querySelector(".searh ul")
let status_server = false;
let search = "";
document.querySelector(".searh-input").addEventListener('input', (e) => {
    section.innerHTML = "";
    search = e.target.value
    if (status_server == false) {
        status_server = true
        setTimeout(() => {
            status_server = false;
            if (search == ""){
                return false;
            }
            $.ajax({
                type: "POST",
                url: "/search",
                data: {
                    'csrfmiddlewaretoken': document.querySelector(
                        '.searh input[name="csrfmiddlewaretoken"]'
                    ).value,
                    "search": search
                },
                success: function (response){
                    for (let i = 0; i<response.product.length; i++){
                        let product = response.product[i]
                        let li = document.createElement('li')
                        li.innerHTML = `<a href="${product['id']}">${product['title']}</a>`
                        section.appendChild(li)
                    }
                },
                error: function (response){}
            })
        }, 2000)
    }
})