let 연습 :string = 'kim';
let 나이 :number = 50;
let 결혼유무 :boolean = false;

let users :string[]= ['jo', 'yun']
let info :{member1 : string} = {member1 : 'kim'}

// 사실 타입스크립트는 변수선언함과 동시에 자동으로 타입 지정해줌

let 회원번호 = 123
let 회원리스트 = [123, 'kim']


let mySong :{[key:string] : string} = { song :'좋은날', singer : '아이유'}

let project: {member :string[], days: number, started : boolean} = {
  member : ['kim', 'park'],
  days : 30,
  started : true,
}