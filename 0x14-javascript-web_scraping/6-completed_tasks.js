#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

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

  const data = JSON.parse(response.body);

  const completed = {};

  for (const task of data) {
    if (task.completed) {
      if (completed[task.userId]) {
        completed[task.userId] += 1;
      } else {
        completed[task.userId] = 1;
      }
    }
  }

  console.log(completed);
});
