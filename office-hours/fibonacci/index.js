/* 
Fibonacci
Implement the Fibonacci function, a famous mathematical equation
that generates a numerical sequence such that each number is the
sum of the previous two. The Fibonacci numbers at index 0 and 1,
coincidentally, have values of 0 and 1. Your function should accept
an argument of which Fibonacci number.

Examples: ​fibonacci(2)​ = 1, ​fibonacci(3)​ = 2, ​fibonacci(4)​ = 3,
​fibonacci(5)​ = 5, etc.
*/

function fibonacci(fibNum) {
  const fibArray = [0, 1];

  for (let i = 2; i <= fibNum; i++) {
    const sum = fibArray[i - 1] + fibArray[i - 2];
    fibArray.push(sum);
  }

  return fibArray[fibNum];
}

// Figure out WHAT to do before we figure HOW to do it.

/* 
  array - first thoughts
  gotta be a loop in there
  gotta be able to access certain positions
  maybe a sum or total variable
  
  we have to build an array until at least the given index.
  the next number is sum of previous two
  index plus previous = next
  it starts with 0 and 1
*/

console.log(fibonacci(6));
