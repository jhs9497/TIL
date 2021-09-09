// Union type
let 음식 :(number | string) = 'kim';

// array 안에 문자, 숫자 들어올 수 있다
let 음식들 :(number | string)[] = [1,2,'햄버거']

// number or string으로 이루어진 array 들어온다는 뜻
let 소괄호안치면 :number | string[] = 2

let 오브젝트 :{ a : string } = { a : '123'}

// any : 모든 type이 들어올 수 있음 but 그럼 TypeScript 쓰는 이유가 없긴함 
// 또한 any가 다른 변수에 할당될 때 그 변수의 type체크도 무효화 시켜버릴 수 있음
let 애니 :any;

애니 - 1
// 에러 안남

// unknown : any처럼 모든 type이 들어올 수 있지만 다른 변수에 들어갈 때 타입체크가 유효함
// 즉 unknown이 더 안정적임
let 언노운 :unknown = 123;

// 언노운 - 1
// 에러 남 


// 엄격한 typescript 체험하기

 let 숫자or문자 :string|number;
 // 숫자or문자 + 1;
 // Union으로 합친 type을 새로운 type으로 인지해서 에러뜸
 // only string이거나 only number만 연산 가능

 let 문자 :string = '1'
 문자 + 1
 // 에러 안남
