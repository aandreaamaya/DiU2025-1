// Selección de elementos del DOM
const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTaskBtn');
const taskList = document.getElementById('taskList');

// Función para agregar una nueva tarea
function addTask() {
    const taskName = taskInput.value.trim();

    if (taskName !== '') {
        // Crear un nuevo elemento de lista
        const taskItem = document.createElement('li');
        taskItem.className = 'task-item';

        // Crear un span para el nombre de la tarea
        const taskNameSpan = document.createElement('span');
        taskNameSpan.className = 'task-name';
        taskNameSpan.textContent = taskName;

        // Botón de eliminar tarea
        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'btn btn-danger btn-sm';
        deleteBtn.textContent = 'Eliminar';

        // Agregar el evento de eliminación al botón
        deleteBtn.addEventListener('click', function() {
            taskList.removeChild(taskItem);
        });

        // Añadir el nombre y el botón de eliminación al elemento de lista
        taskItem.appendChild(taskNameSpan);
        taskItem.appendChild(deleteBtn);

        // Añadir el nuevo elemento a la lista de tareas
        taskList.appendChild(taskItem);

        // Limpiar el campo de entrada
        taskInput.value = '';
    }
}

// Agregar una tarea al hacer clic en el botón
addTaskBtn.addEventListener('click', addTask);

// También agregar la tarea al presionar Enter
taskInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addTask();
    }
});
