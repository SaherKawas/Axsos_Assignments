import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate, Link } from "react-router-dom";

const Update = () => {
  const { id } = useParams();
  const [name, setName] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    axios.get(`http://localhost:8000/api/authors/${id}`)
      .then(res => {
        setName(res.data.name);
      })
      .catch(err => console.error(err));
  }, [id]);

  const updateAuthor = e => {
    e.preventDefault();
    axios.patch(`http://localhost:8000/api/authors/${id}`, { name })
      .then(res => {
        console.log("Author updated:", res.data);
        navigate('/authors');  // back to the list
      })
      .catch(err => console.error(err));
  };

  const handleCancel = () => {
    navigate('/authors');
  };

  return (
    <div>
      <h1>Favorite Authors</h1>
      <Link to="/authors">Home</Link>
      <form onSubmit={updateAuthor}>
        <p>
          <label>Name</label><br />
          <input
            type="text"
            name="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </p>
        <button type="button" onClick={handleCancel}>Cancel</button>
        <button type="submit">Update</button>
      </form>
    </div>
  );
};

export default Update;
