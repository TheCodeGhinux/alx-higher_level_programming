#!/usr/bin/node
const fs = require('fs');
const firstArg = fs.readFileSync(process.argv[2], 'utf8');
const secondArg = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], firstArg + secondArg);
