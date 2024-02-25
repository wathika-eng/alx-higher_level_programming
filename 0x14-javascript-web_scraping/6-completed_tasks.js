#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);

  const completedTasksByUser = {};
  todos.forEach((todo) => {
    if (todo.completed) {
      if (!completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId] = 1;
      } else {
        completedTasksByUser[todo.userId]++;
      }
    }
  });

  Object.entries(completedTasksByUser).forEach(([userId, count]) => {
    console.log(`User ID: ${userId}, Completed Tasks: ${count}`);
  });
});
