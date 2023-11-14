#!/usr/bin/node
function add (a, b) {
  const total = a + b;
  console.log(total);
}

add(Number(process.argv[2]), Number(process.argv[3]));
