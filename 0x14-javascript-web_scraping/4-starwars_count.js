#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
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

  const movies = JSON.parse(body).results;
  let count = 0;
  for (const movieIdx in movies) {
    const movieChars = movies[movieIdx].characters;
    for (const char in movieChars) {
      if (movieChars[char].includes('18')) {
        count++;
      }
    }
  }

  console.log(count);
});
