#!/usr/bin/node

const _number = Number(process.argv[2]);

console.log(Number.isNaN(_number) ? 'Not a number' : 'My number: ' + _number);
