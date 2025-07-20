import React, { useState } from 'react';
import axios from 'axios';

const RegisterForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errors, setErrors] = useState([]);

  const onSubmitHandler = (e) => {
    e.preventDefault();

    const clientErrors = [];
    if (password !== confirmPassword) {
      clientErrors.push("Passwords do not match");
      setErrors(clientErrors);
      return;
    }

    axios.post('http://localhost:8000/api/register', { email, password })
      .then((res) => {
        console.log(res.data);
        setErrors([]); 
        setEmail('');        
        setPassword('');     
        setConfirmPassword('');
        
      })
      .catch((err) => {
        const errorResponse = err.response?.data?.errors;
        const errorArr = [];
        for (const key in errorResponse) {
          if (errorResponse[key].message) {
            errorArr.push(errorResponse[key].message);
          }
        }
        setErrors(errorArr);
      });
  };

  return (
    <div>
      <form onSubmit={onSubmitHandler}>
        {errors.map((err, index) => (
          <p key={index} style={{ color: 'red' }}>{err}</p>
        ))}
        <p>
          <label>Email:</label><br />
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </p>
        <p>
          <label>Password:</label><br />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </p>
        <p>
          <label>Confirm Password:</label><br />
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
        </p>
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default RegisterForm;
