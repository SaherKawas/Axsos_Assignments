import React from 'react';
import LoginForm from './LoginForm';
import RegisterForm from './RegisterForm';

const AuthPage = () => {
  return (
    <div style={{ display: 'flex', gap: '2rem', justifyContent: 'center', padding: '2rem' }}>
      <div>
        <h2>Register</h2>
        <RegisterForm />
      </div>
      <div>
        <h2>Login</h2>
        <LoginForm />
      </div>
    </div>
  );
};

export default AuthPage;
