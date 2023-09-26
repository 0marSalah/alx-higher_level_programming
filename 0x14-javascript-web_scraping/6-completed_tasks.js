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

  const completedCount_per_user = {};

  for (const task of data) {
    if (task.completed) {
      if (completedCount_per_user[task.userId]) {
        completedCount_per_user[task.userId] += 1;
      } else {
        completedCount_per_user[task.userId] = 1;
      }
    }
  }

  console.log(completedCount_per_user);
});
