import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

const AuthorForm = (props) => {
  const [name, setName] = useState("");
  const navigate = useNavigate();

  const onSubmitHandler = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/authors', { name })
      .then(res => {
        console.log(res.data);
        setName("");

        if (props.setAuthors) {
          axios.get('http://localhost:8000/api/authors')
            .then(res => {
              props.setAuthors(res.data);
            });
        }

        navigate('/authors');
      })
      .catch(err => console.log(err));
  };

  const handleCancel = () => {
    navigate('/authors');
  };

  return (
    <>
      <h1>Favorite Authors</h1>
      <Link to="/authors">Home</Link>
      <form onSubmit={onSubmitHandler}>
        <p>
          <label>Name</label><br />
          <input type="text" onChange={(e) => setName(e.target.value)} value={name} />
        </p>
        <button type="button" onClick={handleCancel}>Cancel</button>
        <button type="submit">Create</button>
      </form>
    </>
  );
};

export default AuthorForm;