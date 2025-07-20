import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import LogoutButton from './LogoutButton'; 
import axios from 'axios';

const AuthorsList = () => {
  const [authors, setAuthors] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get('http://localhost:8000/api/authors')
      .then(res => setAuthors(res.data))
      .catch(err => console.error(err));
  }, []);

  const removeFromDom = (authorId) => {
    setAuthors(authors.filter(author => author._id !== authorId));
  };

  const deleteAuthor = (authorId) => {
    axios
      .delete(`http://localhost:8000/api/authors/${authorId}`)
      .then(() => removeFromDom(authorId))
      .catch(err => console.error(err));
  };

  return (
    <div>
      <LogoutButton />
      <h1>Favorite Authors</h1>
      <Link to="/authors/new">Add an author</Link>
      <p>We have quotes by:</p>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Author</th>
            <th>Actions available</th>
          </tr>
        </thead>
        <tbody>
          {authors.map((author) => (
            <tr key={author._id}>
              <td>{author.name}</td>
              <td>
                <button onClick={() => navigate(`/authors/${author._id}/edit`)}>Edit</button>
                <button onClick={() => deleteAuthor(author._id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AuthorsList;
