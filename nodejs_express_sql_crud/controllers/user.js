const User = require('../models/user');

exports.handleUserCreate = async (req, res) => {
  console.log(req.body);
  try {
    const createdUser = await User.create(req.body);
    res.send(createdUser.toJSON())
  } catch(err) {
    console.error('error creating user', err);
    res.status(400).send({ message: "user not created, please note user email is unique" });
  }
};
