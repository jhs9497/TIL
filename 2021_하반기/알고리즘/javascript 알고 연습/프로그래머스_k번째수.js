function solution(array, commands) {
  const answer = [];
  for (let command of commands) {
    const tempArray = array.slice(command[0] - 1, command[1]);
    tempArray.sort(function (a, b) {
      return a - b;
    });
    answer.push(tempArray[command[2] - 1]);
  }
  console.log(answer);
  return answer;
}

array = [1, 5, 2, 6, 3, 7, 4];
commands = [
  [2, 5, 3],
  [4, 4, 1],
  [1, 7, 3],
];
solution(array, commands)