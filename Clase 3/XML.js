// Selección de elementos del DOM
const loadPostsBtn = document.getElementById('loadPostsBtn');
const postList = document.getElementById('postList');

// Función para cargar datos desde la API y mostrarlos en la página
function loadPosts() {
    // Realizar la solicitud GET a la API pública
    fetch('https://jsonplaceholder.typicode.com/posts')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la solicitud: ' + response.statusText);
            }
            return response.json(); // Convertir la respuesta a JSON
        })
        .then(posts => {
            // Limpiar la lista de publicaciones antes de agregar nuevas
            postList.innerHTML = '';
            
            // Recorrer cada publicación y crear un elemento de lista
            posts.forEach(post => {
                const li = document.createElement('li');
                li.textContent = `Título: ${post.title}`;
                postList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Hubo un problema con la solicitud Fetch:', error);
        });
}

// Añadir un evento de clic al botón para cargar las publicaciones
loadPostsBtn.addEventListener('click', loadPosts);
