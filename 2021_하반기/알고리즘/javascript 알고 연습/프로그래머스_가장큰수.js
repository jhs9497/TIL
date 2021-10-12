function solution(numbers) {
  // 모든 number들을 string으로 바꿔주고 문자열을 그대로 연결한 수(b+a) - 바꿔 연결한 수(a+b)가 양수이면
  // ex) b(3) + a(30) - a(30) + b(3) => 330 - 303 = 양수
  // 3 30 순서를 그대로 유지한다.
  let sortList = numbers.map((a) => a + "").sort((a, b) => b + a - (a + b));
  let answer = "";
  for (let n of sortList) {
    answer += String(n);
  }
  return answer[0] === "0" ? "0" : answer;
}
