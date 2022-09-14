// var formRegister = document.getElementById('formRegister'); //obteniendo el formulario de register

// formRegister.onsubmit = function(event) {
//     event.preventDefault(); //previene el comportamiento de mi formulario

//     //creamos una variable con todos los datos del formulario
//     var formulario2 = new FormData(formRegister)
//     console.log(formulario2)
//     // formulario2 = {
//     //     'nombre' : 'alejandro',
//     //     'apellido': 'cataño herrera',
//     //     'email': 'elena@codingdojo.com',
//     //     'password': '1234'
//     // }
//     fetch('/register', {method: 'POST', body: formulario2})
//         .then(response => response.json())

//         .then(data => {
//             console.log(data);

//             var mensajeAlerta2 = document.getElementById('mensajeAlerta2');

//             if(data.message == 'Correcto') {
//                 mensajeAlerta2.innerText = data.message;
//                 mensajeAlerta2.classList.add('alert');
//                 mensajeAlerta2.classList.add('alert-success');
//                 window.location.href = '/dashboard';
//             } else {
//                 mensajeAlerta2.innerText = data.message;
//                 mensajeAlerta2.classList.add('alert');
//                 mensajeAlerta2.classList.add('alert-danger');
//             }
            
            

//         });
// }