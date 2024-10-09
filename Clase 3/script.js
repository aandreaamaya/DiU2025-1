// Seleccionar elementos del DOM
const fetchPokemonButton = document.getElementById('fetchPokemon');
const pokemonNameInput = document.getElementById('pokemonName');
const pokemonInfoDiv = document.getElementById('pokemonInfo');

// Función para buscar un Pokémon en la API
function fetchPokemon() {
    const pokemonName = pokemonNameInput.value.toLowerCase().trim();  // Obtener y limpiar el nombre o ID del Pokémon
    if (!pokemonName) {
        alert('Por favor, ingresa un nombre o ID válido');
        return;
    }

    const url = `https://pokeapi.co/api/v2/pokemon/${pokemonName}`;

    // Hacer la solicitud a la API de Pokémon
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('No se encontró el Pokémon');
            }
            return response.json();
        })
        .then(data => {
            displayPokemonInfo(data);  // Mostrar la información del Pokémon
        })
        .catch(error => {
            pokemonInfoDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
        });
}

// Función para mostrar la información del Pokémon en la página
function displayPokemonInfo(pokemon) {
    const pokemonHTML = `
        <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}">
        <h2>${pokemon.name.charAt(0).toUpperCase() + pokemon.name.slice(1)}</h2>
        <p><strong>ID:</strong> ${pokemon.id}</p>
        <p><strong>Tipo:</strong> ${pokemon.types.map(type => type.type.name).join(', ')}</p>
        <p><strong>Peso:</strong> ${pokemon.weight / 10} kg</p>
        <p><strong>Altura:</strong> ${pokemon.height / 10} m</p>
    `;
    pokemonInfoDiv.innerHTML = pokemonHTML;
}

// Añadir un evento al botón de búsqueda
fetchPokemonButton.addEventListener('click', fetchPokemon);
