#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const filename = process.argv[3];

request(url, (error, response) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(
      `Got an error from the API, status code: ${response.statusCode}`
    );
    return;
  }

  // TODO stream data to filename
  const data = response.body;

  const fs = require('fs');
  fs.writeFile(filename, data, (err) => {
    if (err) throw err;
  });
});
