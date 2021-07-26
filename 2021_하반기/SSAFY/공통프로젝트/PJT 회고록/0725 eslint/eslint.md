## airbnb eslint 설정하기

1. **npx create-react-app myapp --template cra-template-pwa**
2. **VSCode Extensions 설치**
   - ESLint (주황색 로고)
   - Prettier (P & 무지개색 로고)
3. **package.json 들어가서 아래처럼 되어 있는지 확인**

```json
"eslintConfig": {
    "extends": "react-app"
}
```

4. **airbnb eslint 설치** // npx install-peerdeps --dev eslint-config-airbnb
   - 만약 `It seems as if you are using Yarn. Would you like to use Yarn for the installation? (y/n)` 라는게 뜨면 우리는 yarn을 사용하므로`y`를 누르고 엔터키를 누르자.
     그리고 packge.json을 보면 아래와 같은 부분이 추가되어 있을 것이다.
5. **package.json 들어가서 아래처럼 되어 있는지 확인**

```json
"devDependencies": {
    "eslint": "7.2.0",
    "eslint-config-airbnb": "18.2.0",
    "eslint-plugin-import": "^2.21.2",
    "eslint-plugin-jsx-a11y": "^6.3.0",
    "eslint-plugin-react": "^7.20.0",
    "eslint-plugin-react-hooks": "4.0.0"
}
```

6. **root 디렉토리에 (src랑 같은 선상으로) .eslintrc.js 파일 생성**

```javascript
module.exports = {
  env: {
    browser: true,
    es6: true,
    node: true,
  },
  extends: ["airbnb"],
};
```

7. **prettier 설치** // npm install --save-dev --save-exact prettier
8. **root 디렉토리에 .prettierrc.js 파일 생성**

```javascript
// .prettierrc.js

module.exports = {
  // 문자열은 홀따옴표(')로 formatting
  singleQuote: true,
  //코드 마지막에 세미콜른이 있게 formatting
  semi: true,
  //탭의 사용을 금하고 스페이스바 사용으로 대체하게 formatting
  useTabs: false,
  // 들여쓰기 너비는 2칸
  tabWidth: 2,
  // 객체나 배열을 작성 할 때, 원소 혹은 key-value의 맨 뒤에 있는 것에도 쉼표를 붙임
  trailingComma: "all",
  // 코드 한줄이 maximum 80칸
  printWidth: 80,
  // 화살표 함수가 하나의 매개변수를 받을 때 괄호를 생략하게 formatting
  arrowParens: "avoid",
};

타옵션 설정을 원하면 -> https://prettier.io/docs/en/options.html
```

9. **eslint-config-prettier & eslint-plugin-prettier 설치** 
   - npm install --save-dev eslint-plugin-prettier eslint-config-prettier
10. **package.json 들어가서 아래처럼 되어 있는지 확인**

```json
"devDependencies": {
    "eslint": "7.2.0",
    "eslint-config-airbnb": "18.2.0",
    "eslint-config-prettier": "^6.11.0",
    "eslint-plugin-import": "^2.21.2",
    "eslint-plugin-jsx-a11y": "^6.3.0",
    "eslint-plugin-prettier": "^3.1.4",
    "eslint-plugin-react": "^7.20.0",
    "eslint-plugin-react-hooks": "4.0.0"
  }
```

11. **eslint.js 수정**

```javascript
// .eslintrc.js
module.exports = {
  env: {
    browser: true,
    es6: true,
    node: true,
  },
  extends: [
    'airbnb',
    'eslint:recommended',
    'plugin:prettier/recommended',
  ],
  rules: {
    'react/jsx-filename-extension': [
      'error',
      {
        extensions: ['.js', '.jsx'],
      },
    ],
    "no-console": 0,
  },
};
```

12. **자동 Formatting 설정**
1. vscode 설정에서 format javascript 검색 후
   - 기본 JavaScript 포맷터를 사용하거나 사용하지 않습니다 .체크 해제
2. Format On Save 검색 후
   - Format On Save 체크 하기
13. **.serviceWorker.js 처럼 eslint 관리 안받아도 되는 파일에는 파일 최상단에 */\* eslint-disable \*/*  추가**
16. **홈페이지 실행이 안되는 경우**

1. package-lock.json 삭제
2. package.json에서 dependencies and/or devDependencies의 eslint 삭제
3. node-modules 폴더 삭제
4. npm install or (yarn 쓰고 있으면 yarn install)



참고 블로그 : https://velog.io/@cookncoding/ESLint-Prettier-Airbnb-Style-Guide%EB%A1%9C-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%84%B8%ED%8C%85%ED%95%98%EA%B8%B0

