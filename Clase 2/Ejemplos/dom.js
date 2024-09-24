// Clase 02
// Manejo de eventos

// Selecciona el botón usando su ID
let boton = document.getElementById('miBoton');

// Añade un listener para el evento 'click'
boton.addEventListener('click', function() {
    alert('¡Has hecho clic en el botón!'); // Muestra un mensaje cuando se hace clic
    document.getElementById('mensaje').textContent = 'El botón fue clickeado!';
});

// Selección de elementos

// Selección de un elemento por ID y cambio de estilo
let elemento = document.getElementById('miDiv');
elemento.style.color = 'blue'; // Cambia el color del texto a azul

// Selección de múltiples elementos por clase y modificación
let elementos = document.getElementsByClassName('elemento');
for (let i = 0; i < elementos.length; i++) {
    elementos[i].addEventListener('click', function() {
        elementos[i].classList.toggle('completed'); // Marca el elemento como completado o lo desmarca
    });
}

// QuerySelector para seleccionar el primer elemento con el selector CSS dado
let primerElemento = document.querySelector('.elemento');
primerElemento.classList.add('highlight'); // Añade una clase para resaltar el primer elemento

// QuerySelectorAll para seleccionar todos los elementos con el selector CSS dado
let todosLosElementos = document.querySelectorAll('.elemento');
todosLosElementos.forEach(function(el) {
    el.addEventListener('mouseover', function() {
        el.style.fontSize = '20px'; // Cambia el tamaño de fuente al pasar el ratón por encima
    });
});

// Manejo de eventos en campos de entrada
let campoTexto = document.getElementById('campoTexto');
campoTexto.addEventListener('keypress', function(event) {
    console.log('Tecla presionada: ' + event.key); // Muestra en la consola la tecla presionada
});

// Prevenir el comportamiento por defecto de un enlace
let enlace = document.getElementById('miEnlace');
enlace.addEventListener('click', function(event) {
    event.preventDefault(); // Prevenir la navegación
    alert('Navegación a Google prevenida');
});

// Cambiar contenido dinámicamente
let cambiarContenidoBtn = document.getElementById('cambiarContenido');
cambiarContenidoBtn.addEventListener('click', function() {
    let nuevoContenido = campoTexto.value;
    document.getElementById('miDiv').textContent = nuevoContenido;
});
