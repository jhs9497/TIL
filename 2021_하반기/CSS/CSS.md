## html 기본

```css
이미지 가운데 정렬 

style="display: block;
       margin: auto;"

글자 가운데 정렬
text-align : center;

특정 문자 강조하기
<p>Front-end <span style="color : red">Developer</span></p>

굵게 처리하기
<strong></strong> 으로 감싸기
font-weight 사용하기
```



## html에 CSS파일 가져와서 관리하기

```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="css/main.css"> // css파일과 연결
</head>
```

class 누르고 컨트롤 + E 누르면 html 파일에서 바로 CSS 수정 가능!



## class, id 사용하기

직접 넣은 스타일 > id > class > 태그   // 순으로 우선순위가 적용됨

```html
// profile.html

<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="CSS/main.css">
</head>
<body>
  <img 
    src="%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif" 
    class="profile"
  >
  <h4 class="title">아라찌</h4>
  <p id="special">Front-end <span style="color : red">Developer</span></p>
  
</body>
</html>
```

```css
// main.css

class 선언
.profile {
  width: 200px;
  margin: auto;
  display: block;
}


.title {
  text-align: center;
  font-size: 26px;
}

ID 선언
#special {        
  text-align: center;
}
```



## 박스 설정

```css
.description {
  text-align: center;
  width: 400px;
  background-color: antiquewhite;
  /*박스 디자인시 자주 쓰는 스타일링*/
  margin: auto;
  display: block;
     block 뜻 : 한 행을 전부 차지해주세요! 즉 그 다음에 오는 친구들은 밑      으로 내려간다 but 이상황에선 지워도 됨 왜냐면 div 태그가 block속성      을 갖고 있기 때문
  padding: 30px;
  border: 4px solid black;
  font-size: 25px;
  border-radius: 5px;
}
```





## 레이아웃 1 float

```css
// 우선 전체를 싸메는 container라는 div박스를 만들어주는 것이 좋다 

float : left; 
float는 공중에 붕 떠서~ 왼쪽에 정렬된다 그러므로 공간을 차지 하지 않음!!
붕 뜨는 속성 해결하기 위해 뒤에 오는 div박스에 clear: both; 사용하기

다만 또 글씨 & 글씨에서는 붕뜨는 속성 적용안되는 일종의 버그!

```



## 레이아웃 2 inline-block

```css
// inline-blokc은 옆으로 배치해주세요!또한 글씨처럼 공백, 엔터키를 렌더링해줌

.left2 {
  display: inline-block;
}
.right {
  display: inline-block;
  vertical-align: top;
  // inline 속성을 갖고 있다면 글자가 baseline으로 기본세팅 되어 있기 떄문에 top으로 바꿔줘야 정상적으로 글자가 제자리 찾아감
}

<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="CSS/main.css">
</head>
<body>
  
  <div class="container">
    <div class="header"></div>
    <div class="left2"></div><!--
 --><div class="right2">
      <p>안녕하세요</p>
    </div>

  </div>
    
</body>
</html>

```



## 블로그형태 만들기

```css
레이아웃은 네모네모 박스들 설계부터 시작!

style="margin: 0px 10px 50px 4px;" // 시계방향으로 상우좌하 설정 가능

```



## 반응형 웹 만들기

- breakpoint
  아주 작은 모바일 576px < 모바일or태블릿 768px < 태블릿 992px < WEB 1200px

```css
style="font-size : 1rem;"
폰트 사이즈를 비율적으로 정해주기

style="font-size: 2em;"
X em = 부모 폰트사이즈의 X 배

vw, vh
현재 내가 보고있는 view의 몇 %를 차지하는지


.CSS 파일

web/모바일에 따른 반응형 먹여주기

.main-title {
    color: white;
    text-align: center;
    font-size: 50px;
}


화면의 폭이 768px(모바일) 이하일 때 아래의 css 적용하도록 하자! 조건문같은 느낌
@media screen and (max-width: 768px){
    .main-title {
        font-size: 30px;
        display: none; // 안보이게 해버리기!
    }
}
```



## 반응형 웹 만들기 2

```html
.html파일


  <div class="explain-container">
  
    <div>
      <h4>Fast Shipping</h4>
      <p>lorem ipsum</p>
    </div>
    <div>
      <h4>Fast Shipping</h4>
      <p>lorem ipsum</p>
    </div>
    <div>
      <h4>Fast Shipping</h4>
      <p>lorem ipsum</p>
    </div>
    <div>
      <h4>Fast Shipping</h4>
      <p>lorem ipsum</p>
    <div style="float: none; clear: both;"></div
       // explain-container 안의 div들한테 float를 먹였을땐 그 아래에 clear:both;를 넣어줘           야 아래부터 float 속성이 깨짐  
           float: none을 또 먹인 이유는 css를 explain-container div 라고 먹였기 때문임
    </div>
    
  </div>

```

```css
.css 파일

// 기본 WEB 환경에서는 일자로 정렬

.explain-container {
  text-align: center;
  margin-top: 70px;
  max-width: 1200px;
  margin: auto;
  margin-top: 70px;
}
.explain-container div {
  margin-top: 40px;
  float: left;
  width: 25%;
}

// 태블릿의 경우 2열 종대

@media screen and (max-width: 992px){
    .explain-container {
      max-width: 800px;
    }
    .explain-container div {
        float: left;
        width: 50%;
    }
}


// 모바일의 경우 세로로 정렬

@media screen and (max-width: 768px){
    .explain-container div {
        float: none;
        width: 100%;
    }
}


* 더 넓은 breakpoint를 보다 위에 설정해준다 
```



## 반응형 웹사이트 만들기 3 / Bootstrap Grid

utilities-spacing 에서 확인 가능!

margin -> mt-5, ml-5, mr-5, mb-5, m-5

padding -> pt, pl, pr, pb, p

Layout - Grid에서 확인

```html
    <div class="container">
      <div class="row">
        <div class="col-md-4">안녕</div>  
          md(768px)이상에서만 4컬럼씩 차지하세요 그 이하에선 세로 정렬
        <div class="col-md-4">안녕</div>
        <div class="col-md-4 order-first">안녕1</div> 순서 정해주기
      </div>
    </div>
```



## clear 속성이란?

float로 붕떠서 안먹히는 margin을 clear줄로 해결하기

``` html
<div style="clear: both"></div>를 내가 float로 이루어진놈 이랑 내가 margin먹이는 놈 사이에 쏙 하고 밀어넣어주면 원하는대로 margin 먹일 수 있음!
```



## navbar 만들기

```html
selector로 편하게 class 부여하기
class li-inline 안에 있는 모든 li 태그는 같은 스타일을 공유합니다.

.css 

.li-inline li{
  display: inline-block;
}

.html

  <nav>  // 기능은 div 태그랑 똑같지만 웹접근성을 위해 nav라고 명시해주자!
         // 유사한놈들로 section, footer 등 있음
    <ul class="li-inline text-center">
      <li><a href="#">IT</a></li>
      <li><a href="#">맛집</a></li>
      <li><a href="#">동물</a></li>
      <li><a href="#">뷰티</a></li>
    </ul>
  </nav>

```

```css
a태그 밑줄 없애기
.css

.li-inline a {
  text-decoration: none;
}

+ a태그 방문 후에 색깔 검은색으로 해주기

.li-inline a:visited {
  color : black;
}
```



## 사이트 대문 만들기

```css
body {
    margin: 0px;
}
기본적으로 body태그는 margin을 머금고 있음 사이트 꽉차게 보일라면 이거 설정해주기!

.main-background {
  width: 100%;
  height: 500px;
  background-image: url(../images/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif);
  background-size: cover;  // background 꽉 채우기
  background-repeat: no-repeat;  // 반복 X
  background-position: center; // 배경이 어디서부터 채워질지 정할수 있음
  background-attachment: fixed; // 스크롤에 따라 여부
}
```



## margin 버그

예를 들어 div박스가 딱 붙어있으면 안쪽 div에 margin을 주더라도 바깥 div에 준 것 처럼 작동함!

margin이 위아래서 오면서 겹쳐도 마찬가지임!

둘 중 하나에 padding 초 살짝 넣어주고 margin 먹이는 방법 가능



## 버튼 디자인

```css
.main-button {
  padding: 10px;  // 버튼 사이즈
  font-size: 18px;
  font-family: fantasy;
  background-color: white;
  border: none;  // 테두리 없애기
  display: block;  // 가운데정렬 1
  margin: auto;  // 가운데정렬 2
}
```



## position

1. 디폴트값은 static인데 꿈쩍안하고 안움직임!

2. position: relatvie 해주면 요소들이 자유롭게 이동 가능!

3. position : fixed 스크롤로 움직여도 그대로 고정!

   left : 20px 

   top : 20px  왼쪽에서 20px, 위에서 20px 이동한 곳에서 달라붙어라!

4. position: absolute

   - 자신의 부모박스가 기준점임!
   - 단 붙게하고 싶은 부모박스에게 
     - position: relative라고 설정해줘야함!
     - 가운데정렬 하는 법
       - .position {
           position: absolute;
           left: 0;
           right: 0;
           margin: auto;
           width: 150px;
         }



## 반응형 박스만들기

```css
max-width : 700px;
단 max-width는 padding은 포함하지 않음! 그렇기 때문에 padding을 부여하면 max-width가 먹히지 않음

-> 이걸 해결하기 위해서 
box-sizing: border-box 
요걸 쓰면 박스크기를 padding과 border까지 포함하게 설정한다!


-> main.css 같은곳에
div {
    box-sizing: border-box;
}
같은 걸 해주면서 기본값 세팅으로 해주는게 좋다
```

