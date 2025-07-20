const express = require('express');
const app = express();
require('dotenv').config();
const cookieParser = require('cookie-parser');
const cors = require('cors');

const connectDB = require('./config/user.config');

const port = process.env.PORT || 8000;

app.use(cors({ credentials: true, origin: 'http://localhost:5173' }));
app.use(cookieParser());
app.use(express.json());

app.use(require('./routes/user.routes'));

connectDB()
  .then(() => {
    console.log("✅ Connected to MongoDB Atlas");
    app.listen(port, () => console.log(`Listening on port: ${port}`));
  })
  .catch(err => {
    console.error("❌ Connection error:", err);
  });
