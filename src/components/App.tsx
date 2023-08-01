import React from 'react';
import pokemon from '../svg/pokemon.svg';
import '../styles/App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={pokemon} className="App-logo" alt="logo" />
        <p>
          Click on the text below to see the pokemon analysis results.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
