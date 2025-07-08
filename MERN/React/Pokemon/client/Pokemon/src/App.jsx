import React, { useState } from 'react';

function App() {
  const [pokemonList, setPokemonList] = useState([]);

  const fetchPokemon = () => {

    fetch('https://pokeapi.co/api/v2/pokemon?limit=807')
      .then(response => response.json())
      .then(data => {
        const names = data.results.map(pokemon => pokemon.name);
        setPokemonList(names);
        setLoading(false);
      })
      .catch(error => {
        console.error("Error fetching Pokémon:", error);
      });
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Pokémon Fetcher</h1>
      <button onClick={fetchPokemon}>Fetch All 807 Pokémon</button>
      <ul>
        {pokemonList.map((name, index) => (
          <li key={index}>{name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;