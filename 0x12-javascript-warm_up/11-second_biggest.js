#!/usr/bin/node

const args = process.argv.slice(2).map(Number).sort((a, b) => a === b ? 0 : (a < b ? 1 : -1));
console.log(args[1] ? args[1] : 0);
