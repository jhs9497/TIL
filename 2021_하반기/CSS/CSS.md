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

