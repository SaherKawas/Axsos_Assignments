import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Tabs from './components/tabs'

function App() {
  const objects = [
    {label:"Tab1",content:"Hello World"},
    {label:"Tab2",content:"Welcome to Axsos Academy"},
    {label:"Tab3",content:"Congratulations"},
 
  ]

  return (
    <>
     <Tabs arr={objects}/>
    </>
  )
}

export default App