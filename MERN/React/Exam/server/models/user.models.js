const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

const UserSchema = new mongoose.Schema({
  email: {
  type: String,
  required: [true, "Email is required"],
  unique: true,
  match: [/^\S+@\S+\.\S+$/, "Please enter a valid email address"]
},
password: {
  type: String,
  required: [true, "Password is required"],
  minlength: [6, "Password must be at least 6 characters"]
},
}, { timestamps: true });

UserSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();
  try {
    this.password = await bcrypt.hash(this.password, 10);
    next();
  } catch(err) {
    next(err);
  }
});

module.exports = mongoose.model('user.models', UserSchema);
