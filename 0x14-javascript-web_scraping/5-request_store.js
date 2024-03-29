#!/usr/bin/node
const request = require('request');
const fs = require('fs');
if (process.argv.length !== 4) {
  console.error('Usage: node 5-request_store.js <url> <filepath>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const filePath = process.argv[3];
request(apiUrl).pipe(fs.createWriteStream(filePath));
