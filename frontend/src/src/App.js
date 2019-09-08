import React from 'react';
import logo from './csesoc_logo.png';
import './App.css';
import RoomStatus from './roomStatus'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <RoomStatus/>
      </header>
    </div>
  );
}

export default App;
