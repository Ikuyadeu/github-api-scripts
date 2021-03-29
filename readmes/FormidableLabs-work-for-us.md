Come work for us
===========

For senior positions we don't want to accept resumés as all good candidates should have production code, use github etc. Only allow submission via JSON / POST request.

A properly formatted submission looks like:

    var request = require('request');
    request('http://localhost:5000', {
      method: 'POST',
      json: {
        name: "Ryan Eastridge",
        email: "ryan@eastridge.me",
        github: "eastridge",
        code: [
          "url_one",
          "url_two",
          "url_three"
        ],
        links: [
          "url_one",
          "url_two",
          "url_three"
        ]
      }
    }, function() {
      console.log(arguments);
    });