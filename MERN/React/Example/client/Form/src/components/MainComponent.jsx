import React from "react";

const Movies = (props) =>{
    const movieList = ["Die Hard", "Jaws", "Mission Impossible"];
    const {movies}= props
    return(
        <ul>
            {
                movieList.map((item, i)=>
                <li key={i}>{item}</li>)
            }

        </ul>
    );
}
export default Movies;