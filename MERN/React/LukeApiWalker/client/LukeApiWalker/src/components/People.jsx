import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const People = () => {
  const { id } = useParams();
  const [person, setPerson] = useState(null);
  const [error, setError] = useState(null); // 👈 for error tracking
  const [loading, setLoading] = useState(true); // 👈 for loading state

  useEffect(() => {
    setLoading(true);
    setError(null);
    setPerson(null);

    fetch(`https://swapi.tech/api/people/${id}`)
      .then((res) => res.json())
      .then((data) => {
        if (data.result && data.result.properties) {
          setPerson(data.result.properties);
        } else {
          setError("These aren't the droids you're looking for.");
        }
      })
      .catch((err) => {
        console.error(err);
        setError("These aren't the droids you're looking for.");
      })
      .finally(() => {
        setLoading(false);
      });
  }, [id]);

  if (loading) return <p>Loading...</p>;

  if (error) {
    return (
      <div style={{ textAlign: "center", color: "red" }}>
        <p style={{ fontSize: "1.2rem" }}>{error}</p>
        <img
          src="https://media.giphy.com/media/l2JHRhAtnJSDNJ2py/giphy.gif"
          alt="Obi-Wan Kenobi"
          style={{ width: "300px", marginTop: "10px", borderRadius: "8px" }}
        />
      </div>
    );
  }

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
