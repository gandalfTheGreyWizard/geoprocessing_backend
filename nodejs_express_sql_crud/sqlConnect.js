const dotenv = require('dotenv');
dotenv.config();
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize({
  dialect: 'mysql',
  database: process.env.MYSQL_DATABASE,
  username: process.env.MYSQL_USERNAME,
  password: process.env.MYSQL_PASSWORD,
  host: process.env.MYSQL_HOST,
});

(async () => {
  await sequelize.sync({ force: true });
  console.log('models synced');
})();
module.exports = sequelize;
