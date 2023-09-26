#!/usr/bin/node

const request = require('request');

const fid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + fid;

const assert = (err, status) => {
  if (err) {
    console.error('Error fetching data:', err);
    return;
  }

  if (status !== 200) {
    console.error(`Got an error from the API, status code: ${status}`);
  }
};

request(url, function (error, response, body) {
  assert(error, response.statusCode);
  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    assert(error, response.statusCode);
    console.log(JSON.parse(body).name);
    if (index + 1 < characters.length) {
      printCharacters(characters, index + 1);
    }
  });
}
