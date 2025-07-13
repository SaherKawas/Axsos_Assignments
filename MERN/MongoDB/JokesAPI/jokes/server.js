const dotenv = require("dotenv");
dotenv.config(); 

const express = require("express");
const app = express();

const jokeRoutes = require("./routes/jokes.routes");
require("./config/mongoose.config");

app.use(express.json());
app.use(jokeRoutes);

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});