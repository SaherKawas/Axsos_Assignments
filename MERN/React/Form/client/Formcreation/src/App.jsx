import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserForm from './components/UserForm'

function App() {
  

  return (
    <>
      <div className="App">
        <h1>User Registration</h1>
        <UserForm />
      </div>
    </>
  )
}

export default App
