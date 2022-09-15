var formLogin = document.getElementById('formLogin'); //obteniendo el formulario

//vamos a escuchar cuando se realice el evento ON SUBMIT
formLogin.onsubmit = function(event) {
    event.preventDefault(); //previene el comportamiento de mi formulario

    //creamos una variable con todos los datos del formulario
    var formulario = new FormData(formLogin)

    // formulario = {
    //     'email': 'elena@codingdojo.com',
    //     'password': '1234'
    // }
    fetch('/login/login_user/', {method: 'POST', body: formulario})
        .then(response => response.json())

        .then(data => {
            console.log(data);

            var mensajeAlerta = document.getElementById('mensajeAlerta');

            if(data.message == 'Correcto') {
                mensajeAlerta.innerText = data.message;
                mensajeAlerta.classList.add('alert');
                mensajeAlerta.classList.add('alert-success');
                window.location.href = '/dashboard';
            } else {
                mensajeAlerta.innerText = data.message;
                mensajeAlerta.classList.add('alert');
                mensajeAlerta.classList.add('alert-danger');
            }
            
            

        });
}



