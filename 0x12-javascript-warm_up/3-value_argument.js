#!/usr/bin/node

const { argv } = require('node:process');
const arguments = argv.slice(2);

if (!arguments.at(0)) { console.log('No argument'); } else { console.log(arguments.at(0)); }
