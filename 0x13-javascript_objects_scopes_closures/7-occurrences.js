#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let c = 0;

  for (let i = 0; i < list.length; i++) {
    c = (list[i] === searchElement ? c + 1 : c);
  }

  return c;
};
