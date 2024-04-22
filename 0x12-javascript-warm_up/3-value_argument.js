#!/usr/bin/node

const { argv } = require('node:process');

const arg = argv.at(2);
console.log(arg === undefined ? 'No argument' : arg);
