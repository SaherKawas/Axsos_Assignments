const User = require('../models/user.models');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

const secret = process.env.SECRET_KEY || 'secretkey';

module.exports = {
  register: async (req, res) => {
    try {
      const user = await User.create(req.body);
      const userToken = jwt.sign({ id: user._id }, secret);
      res.cookie('usertoken', userToken, { httpOnly: true }).json({ msg: 'success', user });
    } catch (err) {
      res.status(400).json(err);
    }
  },

  login: async (req, res) => {
  console.log("👉 Login request body:", req.body); // Check if email and password are coming through

  const user = await User.findOne({ email: req.body.email });
  if (!user) {
    console.log("❌ User not found for email:", req.body.email);
    return res.status(400).json({ error: "User not found" });
  }

  const validPassword = await bcrypt.compare(req.body.password, user.password);
  if (!validPassword) {
    console.log("❌ Invalid password for user:", req.body.email);
    return res.status(400).json({ error: "Invalid password" });
  }

  const userToken = jwt.sign({ id: user._id }, secret);
  res.cookie('usertoken', userToken, { httpOnly: true }).json({ msg: 'success' });
},

  logout: (req, res) => {
    res.clearCookie('usertoken');
    res.sendStatus(200);
  }
}
