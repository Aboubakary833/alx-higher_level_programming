#!/usr/bin/node

const size = Number(process.argv[2]);

if (Number.isNaN(size)) { console.log('Missing size'); } else {
  for (let i = 0; i < size; i++) {
    let repr = '';
    for (let j = 0; j < size; j++) { repr += 'X'; }
    console.log(repr);
  }
}
