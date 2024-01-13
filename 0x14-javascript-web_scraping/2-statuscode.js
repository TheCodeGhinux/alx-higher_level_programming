#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: node 2-statuscode.js <link>')
  process.exit(1)
}

const linkPath = process.argv[2]
request.get(linkPath, (error, response) => {
  if (error) {
    console.error(error)
  } else {
    console.log(`code: ${response.statusCode}`);
  }
})