function sum(a, b) {
  return a + b;
}

function divide(a, b) {
  return a / b;
}

function calculate(fn, prev) {
  return function (param) {
    return fn(prev, param)
  };
}

const sumWith100 = calculate(sum, 100);
const divideBy100 = calculate(divide, 100);
console.log(sumWith100(20)); //120
divideBy100(20); //5