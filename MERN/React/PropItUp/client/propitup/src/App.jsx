import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import PersonCard from './components/PersonCard'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <PersonCard firstName= "Jane" lastName= "Doe" age= {45} hairColor= "black" />
      <PersonCard firstName= "John" lastName= "Smith" age= {88} hairColor= "brown" />
      <PersonCard firstName= "Millard" lastName= "Fillmore" age= {50} hairColor= "brown" />
      <PersonCard firstName= "Maria" lastName= "Smith" age= {62} hairColor= "brown" />
    </>
  )
}

export default App
