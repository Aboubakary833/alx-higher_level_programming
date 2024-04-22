#!/usr/bin/node

const { argv } = require('node:process');

const __len = argv.length;
console.log(__len === 2 ? 'No argument' : argv.at(2));
