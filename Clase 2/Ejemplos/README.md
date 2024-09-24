Este ejemplo demuestra el uso básico de manipulación del DOM y manejo de eventos en JavaScript, utilizando un archivo HTML (`dom.html`) y un archivo JavaScript (`dom.js`).

Estructura básica:

1. Botón para manejo de eventos:
   - Un botón simple que se utiliza para demostrar cómo manejar eventos de `click` en JavaScript.

2. Lista de elementos (`<ul>`):
   - Una lista de elementos con la clase `elemento` que se usa para mostrar cómo seleccionar y modificar elementos del DOM utilizando JavaScript.

3. Div con ID `miDiv`:
   - Un contenedor `<div>` que se identifica con un ID (`miDiv`). Este elemento se utiliza para modificar su contenido y estilo dinámicamente a través de JavaScript.

4. Campo de entrada (`<input>`):
   - Un campo de entrada que captura eventos de teclado (keypress). Se utiliza para demostrar cómo reaccionar a las entradas del usuario en tiempo real.

5. Enlace (`<a>`):
   - Un enlace que se utiliza para demostrar cómo prevenir su comportamiento por defecto (navegación a otra página) mediante JavaScript.

6. Segundo botón para cambiar contenido:
   - Un segundo botón que se utiliza para demostrar cómo cambiar dinámicamente el contenido de un elemento (`miDiv`) en función de la entrada del usuario.


 Manejo de Eventos:

1. Click en botón:
   - Al hacer clic en el botón, se muestra una alerta y se cambia el texto de un párrafo en la página.

2. Click en lista de tareas:
   - Al hacer clic en un elemento de la lista, se alterna la clase `completed`, lo que tacha o recupera el estilo de la tarea.

3. Mouseover en lista:
   - Cuando el ratón pasa sobre un elemento de la lista, el tamaño de la fuente aumenta, demostrando cómo manejar el evento `mouseover`.

4. Prevenir navegación:
   - El comportamiento por defecto de un enlace (navegación a otra página) se previene, mostrando en su lugar una alerta.

5. Cambiar contenido:
   - El texto introducido en el campo de entrada se coloca dinámicamente en un `div` cuando se hace clic en el segundo botón.

 Selección de Elementos:

1. `getElementById`:
   - Se utiliza para seleccionar un único elemento por su ID y modificar su estilo.

2. `getElementsByClassName`:
   - Se utiliza para seleccionar múltiples elementos por su clase y aplicar cambios a todos ellos.

3. `querySelector`:
   - Se utiliza para seleccionar el primer elemento que coincide con un selector CSS y modificarlo.

4. `querySelectorAll`:
   - Se utiliza para seleccionar todos los elementos que coinciden con un selector CSS específico y aplicar cambios a cada uno de ellos.

