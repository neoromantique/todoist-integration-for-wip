'use strict';

module.exports = (app, db) => {
const eventHandler = require(process.cwd() + '/app/controllers/eventController.js');
const bodyParser = require('body-parser');

  app.route('/')
    .get((req, res) => {
      res.sendStatus(200);
    });

  app.route('/')
    .post(eventHandler)
};
