var x = "global";

function foo() {
  var x = "local";
  return () => {
    console.log(x);
  };
}
const test = foo();

test();
