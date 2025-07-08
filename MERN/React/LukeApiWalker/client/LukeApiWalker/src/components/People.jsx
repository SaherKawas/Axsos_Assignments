import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const People = () => {
  const { id } = useParams();
  const [person, setPerson] = useState(null);

  useEffect(() => {
    fetch(`https://swapi.tech/api/people/${id}`)
      .then(res => res.json())
      .then(data => {
        if (data.result) {
          setPerson(data.result.properties);
        } else {
          setPerson(null);
        }
      })
      .catch(err => {
        console.error(err);
        setPerson(null);
      });
  }, [id]);

  if (!person) return <p>Loading...</p>;

  return (
    <div>
      <h2>{person.name}</h2>
      <p>Height: {person.height}</p>
      <p>Mass: {person.mass}</p>
      <p>Birth Year: {person.birth_year}</p>
    </div>
  );
};

export default People;
