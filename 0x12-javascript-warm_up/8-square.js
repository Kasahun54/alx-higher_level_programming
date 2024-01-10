#!/usr/bin/node
let args = process.argv[2];
if (isNaN(Number(args))) {
  console.log('Missing size');
} else {
  for (let a = 0; a < Number(args); a++) {
    console.log('X'.repeat(args));
  }
}
