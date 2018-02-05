function eventHandler(req, res) {
  if (req.body.event_name == "item:added") {
    let freq =
      req.body.initiator.full_name + " Has added a new task called: " +
      req.body.event_data.content;
    console.log(freq);
    res.sendStatus(200);
  } else if (req.body.event_name == "item:completed") {
    let freq =
      req.body.initiator.full_name + " Has added a new task called: " +
      req.body.event_data.content;
    console.log(freq);
    res.sendStatus(200);
  } else { 
      console.log(req.body.event_name)
      res.sendStatus(502); 
    }
}

module.exports = eventHandler;
