#!/usr/bin/node
//task 10
exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
