const pokemonListElement = document.getElementById('pokemonList');
const pokemonDetailsElement = document.getElementById('pokemonDetails');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
const pokemonTypeSelect = document.getElementById('pokemonType');
const filterButton = document.getElementById('filterButton');
let currentUrl = 'https://pokeapi.co/api/v2/pokemon?limit=10';
let previousUrl = null;
let nextUrl = null;

// Mapeamento dos tipos de Pokémon para português
const typeTranslations = {
    normal: 'Normal',
    fighting: 'Lutador',
    flying: 'Voador',
    poison: 'Venenoso',
    ground: 'Terrestre',
    rock: 'Pedra',
    bug: 'Inseto',
    ghost: 'Fantasma',
    steel: 'Aço',
    fire: 'Fogo',
    water: 'Água',
    grass: 'Grama',
    electric: 'Elétrico',
    psychic: 'Psíquico',
    ice: 'Gelo',
    dragon: 'Dragão',
    dark: 'Sombrio',
    fairy: 'Fada'
};

// Função para buscar a lista de Pokémon
async function fetchPokemonList(url) {
    const response = await fetch(url);
    const data = await response.json();
    previousUrl = data.previous;
    nextUrl = data.next;

    // Habilitar/desabilitar os botões de paginação
    prevButton.disabled = previousUrl === null;
    nextButton.disabled = nextUrl === null;

    displayPokemonList(data.results);
}

// Função para exibir a lista de Pokémon
function displayPokemonList(pokemonList) {
    pokemonListElement.innerHTML = '<ul>' + pokemonList.map(pokemon => `
        <li onclick="fetchPokemonDetails('${pokemon.url}')">${pokemon.name}</li>
    `).join('') + '</ul>';
}

// Função para buscar e exibir detalhes de um Pokémon
async function fetchPokemonDetails(url) {
    const response = await fetch(url);
    const pokemon = await response.json();

    displayPokemonDetails(pokemon);
}

// Função para exibir detalhes do Pokémon
function displayPokemonDetails(pokemon) {
    pokemonDetailsElement.innerHTML = `
        <h2>${pokemon.name.toUpperCase()}</h2>
        <p><strong>ID:</strong> ${pokemon.id}</p>
        <p><strong>Altura:</strong> ${pokemon.height / 10} m</p>
        <p><strong>Peso:</strong> ${pokemon.weight / 10} kg</p>
        <p><strong>Tipos:</strong> ${pokemon.types.map(t => translateType(t.type.name)).join(', ')}</p>
        <p><strong>Habilidades:</strong> ${pokemon.abilities.map(a => a.ability.name).join(', ')}</p>
    `;
}

// Função para buscar Pokémon por nome
async function searchPokemon() {
    const searchTerm = searchInput.value.toLowerCase();
    if (!searchTerm) {
        alert("Por favor, digite o nome de um Pokémon");
        return;
    }

    const url = `https://pokeapi.co/api/v2/pokemon/${searchTerm}`;
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error("Pokémon não encontrado");
        }
        const pokemon = await response.json();
        displayPokemonDetails(pokemon);
    } catch (error) {
        alert(error.message);
    }
}

// Função para buscar tipos de Pokémon e popular o seletor
async function fetchPokemonTypes() {
    const response = await fetch('https://pokeapi.co/api/v2/type');
    const data = await response.json();
    
    data.results.forEach(type => {
        const option = document.createElement('option');
        option.value = type.name;
        option.text = translateType(type.name);
        pokemonTypeSelect.appendChild(option);
    });
}

// Função para buscar Pokémon por tipo
async function filterPokemonByType() {
    const selectedType = pokemonTypeSelect.value;
    if (!selectedType) {
        alert("Por favor, selecione um tipo de Pokémon");
        return;
    }

    const url = `https://pokeapi.co/api/v2/type/${selectedType}`;
    try {
        const response = await fetch(url);
        const data = await response.json();

        const pokemonList = data.pokemon.map(p => p.pokemon);
        displayPokemonList(pokemonList);
    } catch (error) {
        alert("Erro ao buscar Pokémon por tipo");
    }
}

// Função para traduzir tipos de Pokémon para português
function translateType(type) {
    return typeTranslations[type] || type;
}

// Eventos dos botões de paginação
prevButton.addEventListener('click', () => {
    if (previousUrl) {
        fetchPokemonList(previousUrl);
    }
});

nextButton.addEventListener('click', () => {
    if (nextUrl) {
        fetchPokemonList(nextUrl);
    }
});

// Evento de pesquisa
searchButton.addEventListener('click', searchPokemon);

// Evento de filtro por tipo
filterButton.addEventListener('click', filterPokemonByType);

// Inicialização
fetchPokemonList(currentUrl);
fetchPokemonTypes(); // Carregar os tipos de Pokémon no seletor
