require('dotenv').config();
const mongoose = require('mongoose');

const encodedPassword = encodeURIComponent(process.env.ATLAS_PASSWORD);

const uri = `mongodb+srv://${process.env.ATLAS_USERNAME}:${encodedPassword}@cluster0.fkoo3md.mongodb.net/${process.env.DB}?retryWrites=true&w=majority&appName=Cluster0`;

mongoose.connect(uri)
  .then(() => console.log("✅ Connected to MongoDB Atlas"))
  .catch(err => console.log("❌ Connection error:", err));

module.exports = mongoose;
