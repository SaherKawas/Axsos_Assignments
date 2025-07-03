import React, {useState} from "react";

const PersonCard= (props)=>{

    const {firstName, lastName, age, hairColor}= props

    const [counter, setCounter] = useState(0)

    const [currentAge, setCurrentAge] = useState(age);


    const incrementClicks =()=>{
        setCounter(counter + 1);
        setCurrentAge(currentAge + 1);
    }
    return(
        <>
        <h1>{lastName}, {firstName}</h1>
        <p>Age: {currentAge}</p>
        <p> Hair color: {hairColor}</p>
        <p>{counter}</p>
        <button onClick={incrementClicks}>Birthday Button for {firstName} {lastName}</button>
        </>
    )
}

export default PersonCard;