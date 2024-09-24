        // Funcion para cargar datos desde una API pública usando XMLHttpRequest
        function cargarDatos() {
            var xhr = new XMLHttpRequest();  // Crear una nueva instancia de XMLHttpRequest
            
            xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts/1', true);  // Configurar la solicitud
            
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    console.log(xhr.responseText);  // Procesar la respuesta si la solicitud se completó correctamente
                }
            };
            
            xhr.send();  // Enviar la solicitud
        }

        cargarDatos();  // Llamar a la función para cargar los datos