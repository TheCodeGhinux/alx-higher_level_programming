#!/usr/bin/node
function nbOccurences (list, searchElement) {
  return list.reduce(
    (count, current) => (current === searchElement ? count + 1 : count),
    0
  );
}
exports.modules = nbOccurences;
