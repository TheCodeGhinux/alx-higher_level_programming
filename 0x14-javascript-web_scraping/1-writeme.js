#!/usr/bin/node
const fs = require('fs');
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writefile.js <file_path> <content_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];
fs.writeFile(filePath, content, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
