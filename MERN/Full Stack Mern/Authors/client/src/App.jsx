import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AuthPage from './components/Authpage';
import AuthorsList from './components/AuthorsList';
import AuthorForm from './components/AuthorForm';
import Update from './views/Update';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AuthPage />} />
        <Route path="/authors" element={<AuthorsList />} />
        <Route path="/authors/new" element={<AuthorForm />} />
        <Route path="/authors/:id/edit" element={<Update />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
