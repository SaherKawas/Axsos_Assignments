import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import HomeComponent from './components/HomeComponent'

function App() {
const movies = ["Die Hard", "Jaws", "Mission Impossible"]
  return (
    <>
      <div className="App">
        <h1>User Sign Up</h1>
        <HomeComponent />
        <MainComponent movies={movies} message={currentmessage}/>
      </div>
    </>
  )
}

export default App
