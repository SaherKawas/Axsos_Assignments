import React from "react";
import { useParams } from "react-router-dom";

const Number=()=>{
    const {number} = useParams();
    const isNumber = !isNaN(+number);

    return(
        <>
            <div>
                {isNumber ? (
                        <h2>The number is: {number}</h2>
                    ) : (
                        <h2>"{number}" is not a number</h2>
                    )}            
            </div>
        </>
    )
}
export default Number;
