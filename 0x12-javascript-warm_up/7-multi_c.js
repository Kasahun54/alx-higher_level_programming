#!/usr/bin/node
let args = process.argv[2];
if (isNaN(Number(args))) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < Number(args); a++) {
    console.log('C is fun');
  }
}
