#!/usr/bin/node

function second (myArray) {
  if (myArray.length === 2 || myArray.length === 3) {
    return (0);
  }

  let bigest = myArray[2];
  let secondbig = myArray[3];

  for (let i = 2; i < myArray.length; i++) {
    if (myArray[i] > max) {
      secondbig = bigest;
      bigest = myArray[i];
    } else if (myArray[i] > secondbig && myArray[i] < bigest) {
      secondbig = myArray[i];
    }
  }
  return (secondbig);
}

console.log(second(process.argv));
