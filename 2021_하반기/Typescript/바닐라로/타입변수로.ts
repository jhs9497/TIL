// type 변수, 대문자로 시작하는게 rule
type AnimalType = string | number | undefined;

let 동물 :AnimalType = '사자'
동물 = 2
동물 = undefined

// 다 됨!


// 타입스크립트에서는 object안의 value값도 control 가능
// readonly 쓰면 value값 수정 불가능(은 아니고 에러만 띄워줌! .js가면 수정은 되어있음 ㅎㅎ)
type Girlfriend = {
  readonly name : string
}

const 여친 :Girlfriend = {
  name : '미진'
}


// type 합치기
type Name = string;
type Age = number;
type Person = Name | Age

type PositionX = { x : number };
type PositionY = { y : number };
type NewPosition = PositionX & PositionY 
// {x : number, y : number}로 extend 한 것!

let position :NewPosition = { x : 10, y : 20}