import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';  

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();  

  const onSubmitHandler = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/login', { email, password })
      .then(res => {
        console.log(res.data);
        setError('');
        navigate('/dashboard');  
      })
      .catch(err => {
        setError("Invalid email or password");
      });
  };

  return (
    <div>
      <form onSubmit={onSubmitHandler}>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <p>
          <label>Email:</label><br />
          <input type="text" value={email} onChange={e => setEmail(e.target.value)}/>
        </p>
        <p>
          <label>Password:</label><br />
          <input type="password" value={password} onChange={e => setPassword(e.target.value)}/>
        </p>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginForm;
