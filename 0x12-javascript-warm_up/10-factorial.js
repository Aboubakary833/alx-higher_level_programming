#!/usr/bin/node

const arg = Number(process.argv[2]);

console.log(factorOf(arg));

function factorOf (n) {
  if (n < 0) return -1;
  else if (n === 0 || Number.isNaN(n)) { return 1; }
  return n * factorOf(n - 1);
}
