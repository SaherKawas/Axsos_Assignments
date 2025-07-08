import React from 'react'
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './components/Home'
import { Route, Routes, Link } from 'react-router-dom'
import Number from './components/Number'
import Word from './components/Word'
import Color from './components/Color'


function App() {

  return (
    <>
      <div>
        <Routes>
          <Route path="/home" element= {<Home />}/>
          <Route path="/:number" element={<Number />} />
          <Route path="/word/:word" element={<Word />} />
          <Route path="/:word/:textColor/:bgColor" element={<Color />} />

        </Routes>
      </div>
    </>
  )
}

export default App;
