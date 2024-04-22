#!/usr/bin/node

const { argv } = require('node:process');
const length = argv.length;

console.log(length === 2 ? 'No argument' : argv[2]);
