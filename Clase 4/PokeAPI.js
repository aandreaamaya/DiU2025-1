async function fetchPokemon() {
    const pokemonNameOrId = document.getElementById('pokemonInput').value.toLowerCase().trim();

        if (!pokemonNameOrId){
            alert('Ingresa un nombre o un ID válido');
            return;
        }

    try{
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonNameOrId}`);

        if (!response.ok){
            throw new Error('No se ha encontrado el Pokemón');
        }
        const data = await response.json();
        displayPokemonImage(data);
    }catch (error) {
        document.getElementById('pokemonInfo') .innerHTML = '<p style="color: red;">Error: ${error.message}</p>';
    }
}
    function displayPokemonImage(pokemon){
        const pokemonInfoDiv = document.getElementById('pokemonInfo');

        const pokemonHTML = `
            <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}">
            `;
        pokemonInfoDiv.innerHTML = pokemonHTML;
    }
document.getElementById('searchBtn').addEventListener('click', fetchPokemon);

