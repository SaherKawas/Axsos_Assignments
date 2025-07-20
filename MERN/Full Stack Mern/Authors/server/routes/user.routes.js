const express = require('express');
const router = express.Router();
const UserController = require('../controllers/user.controller');
const AuthorController = require('../controllers/author.controller');

// User routes
router.post('/api/register', UserController.register);
router.post('/api/login', UserController.login);
router.post('/api/logout', UserController.logout);

// Author routes
router.post('/api/authors', AuthorController.createAuthor);
router.get('/api/authors', AuthorController.getAllAuthors);
router.get('/api/authors/:id', AuthorController.getAuthor);
router.patch('/api/authors/:id', AuthorController.updateAuthor);
router.delete('/api/authors/:id', AuthorController.deleteAuthor);

module.exports = router;
