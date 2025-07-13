const express = require("express");
const router = express.Router();
const jokeController = require("../controllers/jokes.controller");

router.get("/api/jokes", jokeController.getAllJokes);
router.get("/api/jokes/:id", jokeController.getOneJoke);
router.post("/api/jokes", jokeController.createJoke);
router.put("/api/jokes/:id", jokeController.updateJoke);
router.delete("/api/jokes/:id", jokeController.deleteJoke);

module.exports = router;
