function 내함수(x) {
    if (typeof x === 'number') {
        return x + 1;
    }
    else {
        return x + '1';
    }
}
내함수(123);
function 내함수2(x) {
    let arr = [];
    if (typeof x === 'number') {
        arr[0] = x;
    }
    else {
        return;
    }
}
내함수2(123);
// narrowing이 귀찮다 -> assertion (덮어 씌우기)
function 내함수3(x) {
    let array = [];
    array[0] = x; // 왼쪽에 있는 변수를 오른쪽 type으로 덮어씌워주세요
}
// as 문법의 용도
// 1. Narrowing 할 때 써야한다.
// 2. 무슨 타입이 들어올지 100% 확실할 때 써야한다. -> 사실상 ts 기능 상실하는거임
내함수3(555);
