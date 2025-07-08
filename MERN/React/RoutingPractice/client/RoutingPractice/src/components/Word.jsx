import React from "react";
import { useParams } from "react-router-dom";

const Word=()=>{
    const {word} = useParams();

return(
        <>
            <div>
                
                <h2>The word is: {word}</h2>
                             
            </div>
        </>
    )
}
export default Word;