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

request(url, async (error, response) => {
  assert(error, response.statusCode);

  const characters = await JSON.parse(response.body).characters;
  for (const character of characters) {
    request(character, async (error, response) => {
      assert(error, response.statusCode);

      const name = await JSON.parse(response.body).name;
      console.log(name);
    });
  }
});
