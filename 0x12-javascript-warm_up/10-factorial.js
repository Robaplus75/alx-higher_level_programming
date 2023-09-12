#!/usr/bin/node

function fact (number) {
  if (isNaN(parseInt(number))) {
    return (1);
  }
  if (number === 1) {
    return (1);
  }
  return (number * fact(number - 1));
}

console.log(fact(parseInt(process.argv[2])));
