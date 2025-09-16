const { json } = require('express');
const mysql = require('mysql2/promise')
const { Sequelize } = require('sequelize');
// Create the connection to database
const User = require('../models/user');
exports.returnIndex = async (req, res) => {
  try {
    await sequelize.authenticate();
  } catch(err) {
    console.error(err);
  }
  responseObject = {
    'message': 'hello world!'
  }
  res.send(responseObject);
}
