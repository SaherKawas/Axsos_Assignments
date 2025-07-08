import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const Planets = () => {
  const { id } = useParams();
  const [planet, setPlanet] = useState(null);

  useEffect(() => {
    fetch(`https://swapi.tech/api/planets/${id}`)
      .then(res => res.json())
      .then(data => {
        if (data.result) {
          setPlanet(data.result.properties);
        } else {
          setPlanet(null);
        }
      })
      .catch(err => {
        console.log(err);
        setPlanet(null);
      });
  }, [id]);

  if (!planet) return <p>Loading...</p>;

  return (
    <div>
      <h2>{planet.name}</h2>
      <p>Climate: {planet.climate}</p>
      <p>Population: {planet.population}</p>
      <p>Terrain: {planet.terrain}</p>
    </div>
  );
};

export default Planets;