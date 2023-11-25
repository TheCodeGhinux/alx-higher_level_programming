#!/usr/bin/node
function esrever (list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
}
exports.modules = esrever;
