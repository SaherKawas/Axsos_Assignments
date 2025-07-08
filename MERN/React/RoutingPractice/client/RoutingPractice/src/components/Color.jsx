import React from "react";
import { useParams } from "react-router-dom";

const Color=()=>{
    const {word, textColor, bgColor} = useParams();

    const style= {
        color: textColor,
        backgroundColor: bgColor,
        width: '900px'
    }

return(
        <>
            <div>
                
                <h2 style={style}>{word}</h2>
                             
            </div>
        </>
    )
}
export default Color;