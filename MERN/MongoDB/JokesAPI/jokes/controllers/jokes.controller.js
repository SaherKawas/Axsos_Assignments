const Joke = require("../models/jokes.model");

// Get all jokes
const getAllJokes = (req, res) => {
  Joke.find()
    .then(jokes => res.json(jokes))
    .catch(err => res.status(400).json(err));
};

// Get one joke
const getOneJoke = (req, res) => {
  Joke.findById(req.params.id)
    .then(joke => res.json(joke))
    .catch(err => res.status(400).json(err));
};

// Create joke
const createJoke = (req, res) => {
  Joke.create(req.body)
    .then(joke => res.json(joke))
    .catch(err => res.status(400).json(err));
};

// Update joke
const updateJoke = (req, res) => {
  Joke.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true })
    .then(joke => res.json(joke))
    .catch(err => res.status(400).json(err));
};

// Delete joke
const deleteJoke = (req, res) => {
  Joke.findByIdAndDelete(req.params.id)
    .then(result => res.json({ success: true }))
    .catch(err => res.status(400).json(err));
};

module.exports = {
  getAllJokes,
  getOneJoke,
  createJoke,
  updateJoke,
  deleteJoke
};
