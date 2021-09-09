function 함수2(x :number) :number {
  return x * 2
}

함수2(3)


// 함수에서만 쓸 수 있는 void 타입
// return 하기 싫은 함수에서 쓰기!
// void는 텅 비었다는 뜻
// 실수로 return 넣을 시 에러 발생시킴
function 함수3 (x :number) :void{
  1 + 1
}

함수3(10)

// 파라미터 무조건 넣어야 에러 안나는데 파라미터를 옵션으로 주고 싶으면
// 파라미터 뒤에 ? 넣어주기 -> undefined가 들어올 수 있다는 뜻을 의미

function 함수4 (x? :number) :void{
  1 + 1
}

함수4()