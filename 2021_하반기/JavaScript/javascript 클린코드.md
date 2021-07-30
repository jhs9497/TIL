### 사이드 이펙트를 피하세요 (part 1)

함수는 값을 받아서 어떤 일을 하거나 값을 리턴할 때 사이드 이팩트를 만들어냅니다. 사이드 이팩트는 파일에 쓰여질 수도 있고, 전역 변수를 수정할 수 있으며, 실수로 모든 돈을 다른 사람에게 보낼 수도 있습니다.

당신은 때때로 프로그램에서 사이드 이팩트를 만들어야 할 때가 있습니다. 아까 들었던 예들 중 하나인 파일작성을 할 때와 같이 말이죠. 이 때 여러분이 해야할 일은 파일 작성을 하는 한 개의 함수를 만드는 일 입니다. 파일을 작성하는 함수나 클래스가 여러개 존재하면 안됩니다. 반드시 하나만 있어야 합니다.

즉, 어떠한 구조체도 없이 객체 사이의 상태를 공유하거나, 무엇이든 쓸 수 있는 변경 가능한 데이터 유형을 사용하거나, 같은 사이드 이펙트를 만들어내는 것을 여러개 만들거나하면 안됩니다. 여러분들이 이러한 것들을 지키며 코드를 작성한다면 대부분의 다른 개발자들보다 행복할 수 있습니다.

**안좋은 예:**

```javascript
// 아래 함수에 의해 참조되는 전역 변수입니다.
// 이 전역 변수를 사용하는 또 하나의 함수가 있다고 생각해보세요. 이제 이 변수는 배열이 될 것이고, 프로그램을 망가뜨리겠죠.
let name = 'Ryan McDermott';

function splitIntoFirstAndLastName() {
  name = name.split(' ');
}

splitIntoFirstAndLastName();

console.log(name); // ['Ryan', 'McDermott'];
```

**좋은 예:**

```javascript
function splitIntoFirstAndLastName(name) {
  return name.split(' ');
}

const name = 'Ryan McDermott';
const newName = splitIntoFirstAndLastName(name);

console.log(name); // 'Ryan McDermott';
console.log(newName); // ['Ryan', 'McDermott'];
```



### 사이드 이펙트를 피하세요 (part 2)

자바스크립트에서는 기본타입 자료형은 값을 전달하고 객체와 배열은 참조를 전달합니다. 객체와 배열인 경우를 한번 살펴봅시다. 우리가 만든 함수는 장바구니 배열에 변화를 주며 이 변화는 구매목록에 어떤 상품을 추가하는 기능 같은 것을 말합니다. 만약 `장바구니` 배열을 사용하는 어느 다른 함수가 있다면 이러한 추가에 영향을 받습니다. 이것은 좋을 수도 있지만, 안좋을 수도 있습니다. 안좋은 예를 한번 상상해봅시다.

유저가 구매하기 버튼을 눌러 `구매` 함수를 호출합니다. 이는 네트워크 요청을 생성하고 서버에 `장바구니` 배열을 보냅니다. 하지만 네트워크 연결이 좋지않아서 `구매` 함수는 다시한번 네트워크 요청을 보내야 하는 상황이 생겼습니다. 이때, 사용자가 네트워크 요청이 시작되기 전에 실수로 원하지 않는 상품의 "장바구니에 추가" 버튼을 실수로 클릭하면 어떻게될까요? 실수가 있고난 뒤, 네트워크 요청이 시작되면 `장바구니에 추가` 함수 때문에 실수로 변경된 `장바구니` 배열을 서버에 보내게 됩니다.

가장 좋은 방법은 `장바구니에 추가`는 항상 `장바구니` 배열을 복제하여 수정하고 복제본을 반환하는 것입니다. 이렇게하면 장바구니 참조를 보유하고있는 다른 함수가 다른 변경 사항의 영향을 받지 않게됩니다.

이 접근법에대해 말하고 싶은 것이 두가지 있습니다.

1. 실제로 입력된 객체를 수정하고 싶은 경우가 있을 수 있지만 이러한 예제를 생각해보고 적용해보면 그런 경우는 거의 없다는 것을 깨달을 수 있습니다. 그리고 대부분의 것들이 사이드 이펙트 없이 리팩토링 될 수 있습니다.
2. 큰 객체를 복제하는 것은 성능 측면에서 값이 매우 비쌉니다. 운좋게도 이런게 큰 문제가 되지는 않습니다. 왜냐하면 이러한 프로그래밍 접근법을 가능하게해줄 [좋은 라이브러리](https://facebook.github.io/immutable-js/)가 있기 때문입니다. 이는 객체와 배열을 수동으로 복제하는 것처럼 메모리 집약적이지 않게 해주고 빠르게 복제해줍니다.

**Bad:**

```javascript
const addItemToCart = (cart, item) => {
  cart.push({ item, date: Date.now() });
};
```

**Good:**

```javascript
const addItemToCart = (cart, item) => {
  return [...cart, { item, date : Date.now() }];
};
```



### 조건문 작성을 피하세요

조건문 작성을 피하라는 것은 매우 불가능한 일로 보입니다. 이 얘기를 처음 듣는 사람들은 대부분 "`If`문 없이 어떻게 코드를 짜나요?"라고 말합니다. 하지만 다형성을 이용한다면 동일한 작업을 수행할 수 있습니다. 두번째 질문은 보통 "네 좋네요 근데 내가 왜 그렇게 해야하나요?"이죠. 그에 대한 대답은, 앞서 우리가 공부했던 clean code 컨셉에 있습니다. 함수는 단 하나의 일만 수행하여야 합니다. 당신이 함수나 클래스에 `if`문을 쓴다면 그것은 그 함수나 클래스가 한가지 이상의 일을 수행하고 있다고 말하는 것과 같습니다. 기억하세요, 하나의 함수는 딱 하나의 일만 해야합니다.

**안좋은 예:**

```javascript
class Airplane {
  // ...
  getCruisingAltitude() {
    switch (this.type) {
      case '777':
        return this.getMaxAltitude() - this.getPassengerCount();
      case 'Air Force One':
        return this.getMaxAltitude();
      case 'Cessna':
        return this.getMaxAltitude() - this.getFuelExpenditure();
    }
  }
}
```

**좋은 예:**

```javascript
class Airplane {
  // ...
}

class Boeing777 extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getPassengerCount();
  }
}

class AirForceOne extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude();
  }
}

class Cessna extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getFuelExpenditure();
  }
}
```



### 타입-체킹을 피하세요 (part 2)

당신이 문자열, 정수, 배열등 기본 자료형을 사용하고 다형성을 사용할 수 없을 때 여전히 타입-체킹이 필요하다고 느껴진다면 TypeScript를 도입하는 것을 고려해보는 것이 좋습니다. TypeScript는 표준 JavaScript 구문에 정적 타입을 제공하므로 일반 JavaScript의 대안으로 사용하기에 좋습니다. JavaScript에서 타입-체킹을 할 때 문제점은 가짜 `type-safety` 를 얻기위해 작성된 코드를 설명하기 위해서 많은 주석을 달아야한다는 점입니다. JavaScript로 코드를 작성할땐 깔끔하게 코드를 작성하고, 좋은 테스트 코드를 짜야하며 좋은 코드 리뷰를 해야합니다. 그러기 싫다면 그냥 TypeScript(이건 제가 말했듯이, 좋은 대체재입니다!)를 쓰세요.

**안좋은 예:**

```javascript
function combine(val1, val2) {
  if (typeof val1 === 'number' && typeof val2 === 'number' ||
      typeof val1 === 'string' && typeof val2 === 'string') {
    return val1 + val2;
  }
  
  throw new Error('Must be of type String or Number');
}
```

**좋은 예:**

```javascript
function combine(val1, val2) {
  return val1 + val2;
}
```



## **테스트(Testing)**

테스트는 배포하는 것보다 중요합니다. 테스트 없이 배포한다는 것은 당신이 짜놓은 코드가 언제든 오작동해도 이상하지 않다는 얘기와 같습니다. 테스트에 얼마나 시간을 투자할지는 당신이 함께 일하는 팀에 달려있지만 Coverage가 100%라는 것은 개발자들에게 높은 자신감과 안도감을 줍니다. 이 말은 훌륭한 테스트 도구를 보유해야 하는 것 뿐만 아니라 [훌륭한 Coverage 도구](http://gotwarlost.github.io/istanbul/)를 사용해야한다는 것을 의미합니다.

테스트 코드를 작성하지 않는다는 것은 그 무엇도 변명이 될 수 없습니다. 여기 [훌륭하고 많은 JavaScript 테스트 프레임워크들](http://jstherightway.org/#testing-tools) 이 있습니다. 당신의 팀의 기호에 맞는 프레임워크를 고르기만 하면 됩니다. 테스트 프레임워크를 골랐다면 이제부터는 팀의 목표를 모든 새로운 기능/모듈을 짤 때 테스트 코드를 작성하는 것으로 하세요. 만약 테스트 주도 개발 방법론(Test Driven Development, TDD)이 당신에게 맞는 방법이라면 그건 훌륭한 개발 방법이 될 수 있습니다. 그러나 중요한 것은 당신이 어떠한 기능을 개발하거나 코드를 리팩토링 할 때 당신이 정한 Coverage 목표를 달성하는 것에 있습니다.

### 테스트 컨셉

**안좋은 예:**

```javascript
const assert = require('assert');

describe('MakeMomentJSGreatAgain', () => {
  it('handles date boundaries', () => {
    let date;

    date = new MakeMomentJSGreatAgain('1/1/2015');
    date.addDays(30);
    assert.equal('1/31/2015', date);

    date = new MakeMomentJSGreatAgain('2/1/2016');
    date.addDays(28);
    assert.equal('02/29/2016', date);

    date = new MakeMomentJSGreatAgain('2/1/2015');
    date.addDays(28);
    assert.equal('03/01/2015', date);
  });
});
```

**좋은 예:**

```javascript
const assert = require('assert');

describe('MakeMomentJSGreatAgain', () => {
  it('handles 30-day months', () => {
    const date = new MakeMomentJSGreatAgain('1/1/2015');
    date.addDays(30);
    assert.equal('1/31/2015', date);
  });

  it('handles leap year', () => {
    const date = new MakeMomentJSGreatAgain('2/1/2016');
    date.addDays(28);
    assert.equal('02/29/2016', date);
  });

  it('handles non-leap year', () => {
    const date = new MakeMomentJSGreatAgain('2/1/2015');
    date.addDays(28);
    assert.equal('03/01/2015', date);
  });
});
```



## **동시성(Concurrency)**

### Callback 대신 Promise를 사용하세요

Callback은 깔끔하지 않습니다. 그리고 엄청나게 많은 중괄호 중첩을 만들어 냅니다. ES2015/ES6에선 Promise가 내장되어 있습니다. 이걸 쓰세요!

**안좋은 예:**

```javascript
require('request').get('https://en.wikipedia.org/wiki/Robert_Cecil_Martin', (requestErr, response) => {
  if (requestErr) {
    console.error(requestErr);
  } else {
    require('fs').writeFile('article.html', response.body, (writeErr) => {
      if (writeErr) {
        console.error(writeErr);
      } else {
        console.log('File written');
      }
    });
  }
});
```

**좋은 예:**

```javascript
require('request-promise').get('https://en.wikipedia.org/wiki/Robert_Cecil_Martin')
  .then((response) => {
    return require('fs-promise').writeFile('article.html', response);
  })
  .then(() => {
    console.log('File written');
  })
  .catch((err) => {
    console.error(err);
  });
```



### Async/Await은 Promise보다 더욱 깔끔합니다

Promise도 Callback에 비해 정말 깔끔하지만 ES2017/ES8에선 async와 await이 있습니다. 이들은 Callback에대한 더욱 깔끔한 해결책을 줍니다. 오직 필요한 것은 함수앞에 `async`를 붙이는 것 뿐입니다. 그러면 함수를 논리적으로 연결하기위해 더이상 `then`을 쓰지 않아도 됩니다. 만약 당신이 ES2017/ES8 사용할 수 있다면 이것을 사용하세요!

**안좋은 예:**

```javascript
require('request-promise').get('https://en.wikipedia.org/wiki/Robert_Cecil_Martin')
  .then(response => {
    return require('fs-promise').writeFile('article.html', response);
  })
  .then(() => {
    console.log('File written');
  })
  .catch(err => {
    console.error(err);
  })
```

**좋은 예:**

```javascript
async function getCleanCodeArticle() {
  try {
    const response = await require('request-promise').get('https://en.wikipedia.org/wiki/Robert_Cecil_Martin');
    await require('fs-promise').writeFile('article.html', response);
    console.log('File written');
  } catch(err) {
    console.error(err);
  }
}
```



### 함수 호출자와 함수 피호출자는 가깝게 위치시키세요

어떤 함수가 다른 함수를 호출하면 그 함수들은 소스 파일 안에서 서로 수직으로 근접해 있어야 합니다. 이상적으로는 함수 호출자를 함수 피호출자 바로 위에 위치시켜야 합니다. 우리는 코드를 읽을때 신문을 읽듯 위에서 아래로 읽기 때문에 코드를 작성 할 때도 읽을 때를 고려하여 작성 해야합니다.

**안좋은 예:**

```javascript
class PerformanceReview {
  constructor(employee) {
    this.employee = employee;
  }

  lookupPeers() {
    return db.lookup(this.employee, 'peers');
  }

  lookupManager() {
    return db.lookup(this.employee, 'manager');
  }

  getPeerReviews() {
    const peers = this.lookupPeers();
    // ...
  }

  perfReview() {
    this.getPeerReviews();
    this.getManagerReview();
    this.getSelfReview();
  }

  getManagerReview() {
    const manager = this.lookupManager();
  }

  getSelfReview() {
    // ...
  }
}

const review = new PerformanceReview(user);
review.perfReview();
```

**좋은 예:**

```javascript
class PerformanceReview {
  constructor(employee) {
    this.employee = employee;
  }

  perfReview() {
    this.getPeerReviews();
    this.getManagerReview();
    this.getSelfReview();
  }

  getPeerReviews() {
    const peers = this.lookupPeers();
    // ...
  }

  lookupPeers() {
    return db.lookup(this.employee, 'peers');
  }

  getManagerReview() {
    const manager = this.lookupManager();
  }

  lookupManager() {
    return db.lookup(this.employee, 'manager');
  }

  getSelfReview() {
    // ...
  }
}

const review = new PerformanceReview(employee);
review.perfReview();
```



## **주석(Comments)**

### 비즈니스 로직이 복잡한 경우에만 주석을 다세요

주석을 다는것은 사과해야할 일이며 필수적인 것이 아닙니다. 좋은 코드는 *코드 자체*로 말합니다.

**안좋은 예:**

```javascript
function hashIt(data) {
  // 이건 해쉬입니다.
  let hash = 0;

  // lengh는 data의 길이입니다.
  const length = data.length;

  // 데이터의 문자열 개수만큼 반복문을 실행합니다.
  for (let i = 0; i < length; i++) {
    // 문자열 코드를 얻습니다.
    const char = data.charCodeAt(i);
    // 해쉬를 만듭니다.
    hash = ((hash << 5) - hash) + char;
    // 32-bit 정수로 바꿉니다.
    hash &= hash;
  }
}
```

**좋은 예:**

```javascript
function hashIt(data) {
  let hash = 0;
  const length = data.length;

  for (let i = 0; i < length; i++) {
    const char = data.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;

    // 32-bit 정수로 바꿉니다.
    hash &= hash;
  }
}
```

**[⬆ 상단으로](https://github.com/qkraudghgh/clean-code-javascript-ko#목차)**

### 주석으로 된 코드를 남기지 마세요

버전 관리 도구가 존재하기 때문에 코드를 주석으로 남길 이유가 없습니다.

**안좋은 예:**

```javascript
doStuff();
// doOtherStuff();
// doSomeMoreStuff();
// doSoMuchStuff();
```

**좋은 예:**

```javascript
doStuff();
```

**[⬆ 상단으로](https://github.com/qkraudghgh/clean-code-javascript-ko#목차)**

### 코드 기록을 주석으로 남기지 마세요

버전 관리 도구를 이용해야하는 것을 꼭 기억하세요. 죽은 코드도 불필요한 설명도 특히 코드의 기록에 대한 주석도 필요하지 않습니다. 코드의 기록에 대해 보고 싶다면 `git log`를 사용하세요!

**안좋은 예:**

```javascript
/**
 * 2016-12-20: 모나드 제거했음, 이해는 되지 않음 (RM)
 * 2016-10-01: 모나드 쓰는 로직 개선 (JP)
 * 2016-02-03: 타입체킹 하는부분 제거 (LI)
 * 2015-03-14: 버그 수정 (JR)
 */
function combine(a, b) {
  return a + b;
}
```

**좋은 예:**

```javascript
function combine(a, b) {
  return a + b;
}
```

**[⬆ 상단으로](https://github.com/qkraudghgh/clean-code-javascript-ko#목차)**

### 코드의 위치를 설명하지 마세요

이건 정말 쓸데 없습니다. 적절한 들여쓰기와 포맷팅을 하고 함수와 변수의 이름에 의미를 부여하세요.

**안좋은 예:**

```javascript
////////////////////////////////////////////////////////////////////////////////
// 스코프 모델 정의
////////////////////////////////////////////////////////////////////////////////
$scope.model = {
  menu: 'foo',
  nav: 'bar'
};

////////////////////////////////////////////////////////////////////////////////
// actions 설정
////////////////////////////////////////////////////////////////////////////////
const actions = function() {
  // ...
};
```

**좋은 예:**

```javascript
$scope.model = {
  menu: 'foo',
  nav: 'bar'
};

const actions = function() {
  // ...
};
```





무엇을 카피했는지 / 어떤 용도의 인덱스인지



회원가입 실패시 alert에 response.message 보여주기

