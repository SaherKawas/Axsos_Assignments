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
    const user = await User.findOne({ email: req.body.email });
    if (!user) return res.sendStatus(400);

    const validPassword = await bcrypt.compare(req.body.password, user.password);
    if (!validPassword) return res.sendStatus(400);

    const userToken = jwt.sign({ id: user._id }, secret);
    res.cookie('usertoken', userToken, { httpOnly: true }).json({ msg: 'success' });
  },

  logout: (req, res) => {
    res.clearCookie('usertoken');
    res.sendStatus(200);
  }
};
