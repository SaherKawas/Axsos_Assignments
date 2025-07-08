import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Route, Routes } from 'react-router-dom'
import Home from './components/Home'
import Planets from './components/Planets'
import People from './components/People'


function App() {

  return (
    <>
      <div>
        <Routes>
          <Route path="/" element= {<Home />}/>
          <Route path="/people/:id" element={<People />} />
          <Route path="/planets/:id" element={<Planets />} />
        </Routes>
      </div>
    </>
  )
}

export default App
