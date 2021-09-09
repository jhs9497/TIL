let 이름 :string = 'kim';
// 이 변수엔 string(문자)만 들어올 수 있다!

let 어레이 :string[] = ['kim', 'park']
// 이 배열엔 문자형만 들어올 수 있다!

let 이름or숫자 :string | number = 123;
이름or숫자 = '문자'
// 이 배열엔 문자 or 숫자형 가능

type MyType = string | number;
// 타입의 변수화

let 타입변수화 :MyType = '타입은 보통 대문자로 명명함'
// 타입 변수로 먹이기 가능

function 함수(x :number) :number{ // 오른쪽 타입은 어떤 타입으로 리턴되는지 정의
  return x * 2
}

type Member = [number, boolean]; // 어레이에서 무조건 첫 째는 number, 둘 째는 boolean값이 들어와야함
let john:Member = [122, true]


// 객체에 key 값은 무조건 string, value값도 string으로 들어와야 한다!
type MemberObj = {
  [key :string] : string,
}

let hyunsix : MemberObj = { name : '현식', gender : 'Man'}

