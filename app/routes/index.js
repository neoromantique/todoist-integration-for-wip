'use strict';

module.exports = (app, db) => {
  db;
const bodyParser = require('body-parser');

  app.route('/')
    .get((req, res) => {
      res.sendStatus(200);
    });

  app.route('/')
    .post((req, res) => {
      console.log(req.body);
      res.sendStatus(200);
    })
};
