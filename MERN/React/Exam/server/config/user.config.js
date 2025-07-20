const mongoose = require('mongoose');

const encodedPassword = encodeURIComponent(process.env.ATLAS_PASSWORD);
const uri = `mongodb+srv://${process.env.ATLAS_USERNAME}:${encodedPassword}@cluster0.fkoo3md.mongodb.net/${process.env.DB}?retryWrites=true&w=majority&appName=Cluster0`;

const connectDB = () => {
  return mongoose.connect(uri);
};

module.exports = connectDB;
