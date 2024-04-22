#!/usr/bin/node
const count = process.argv.length;
console.log(count === 2 ? 'No argument' : process.argv[2]);
