import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Main from './views/Main';
import Detail from './views/Details';
// import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route element={<Main/>} path="/products/" />
        <Route element={<Detail/>} path="/products/:id" />
      </Routes>
    </div>
  );
}

export default App;
