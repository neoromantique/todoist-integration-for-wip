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
      let freq = 
            req.body.initiator.full_name + " Has added a new task called: "
            + req.body.event_data.content;
      console.log(freq);
      res.sendStatus(200);
    })
};
