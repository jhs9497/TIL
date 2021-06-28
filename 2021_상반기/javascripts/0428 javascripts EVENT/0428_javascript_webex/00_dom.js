// 1. Selection - querySelector / querySelectorAll
// 1-1. window & document
// console.log(window)
// console.log(document)
// console.log(window.document)

// 1-2. querySelector
// const mainHeader = document.querySelector('h1')
// console.log(mainHeader)

// const langHeader = document.querySelector('#lang-header')
// const frameHeader = document.querySelector('#frame-header')
// console.log(mainHeader, langHeader, frameHeader)

// 1-3. querySelectorAll
// const langLi = document.querySelectorAll('.lang')
// console.log(langLi)
// const frameworkLi = document.querySelectorAll('.framework')
// console.log(langLi, frameworkLi)

// 1-4. 여러 개의 요소 -> 첫 번째로 일치하는 요소
// const selectOne = document.querySelector('.lang')
// console.log(selectOne)

// 1-5. 복합 선택자
// const selectDescendant = document.querySelector('body li')
// const selectDescendant = document.querySelectorAll('body li')
// const selectChild = document.querySelector('body > li')
// console.log(selectDescendant) 
// console.log(selectChild) 

// 1-6. getElementById, getElementByClassName 
// const selectSepcialLang = document.getElementById('special-lang')
// const selectAllLangs = document.getElementsByClassName('framework')
// const selectAllLiTags = document.getElementsByTagName('li')
// console.log(selectSepcialLang, selectAllLangs, selectAllLiTags)


// 2. Manipulation
// 2-1. Creation
const header = document.querySelector('#header')
// console.log(header)
// console.dir(header)  // 뭐 할수 있는지 볼 수 있는 명령어
header.style.color = 'red'
header.innerText = '바꿀꺼야!'


// userInput.addEventListener('input', function() {
//   console.log('안녕!')
// }) // 이벤트이름, 실행하고 싶은 함수
// // ex) click, keypress, load

const submitBtn = document.querySelector('#submit-btn')
submitBtn.addEventListener('click', function() {
  const newLi = document.createElement('li')
  const languageList = document.querySelector('#lang-list')
  const userInput = document.querySelector('#user-input')

  newLi.setAttribute('class', 'lang')  // 형제들이랑 똑같게 클래스 넣어주기
  newLi.innerText = userInput.value // 이름 지어주기

  languageList.append(newLi)
})

// const browserHeader = document.createElement('h2')
// const ul = document.createElement('ul')
// const li1 = document.createElement('li')
// const li2 = document.createElement('li')
// const li3 = document.createElement('li')
// console.log(browserHeader, li1, li2, li3) 


// 2-2. innerText & innerHTML / append & appendChild
// browserHeader.innerText = 'Browsers'
// li1.innerText = 'IE'
// li2.innerText = '<strong>FireFox</strong>'
// li3.innerHTML = '<strong>Chrome</strong>'
// console.log(browserHeader, li1, li2, li3)

// 2-3. append DOM 
// const body = document.querySelector('body')
// body.appendChild(browserHeader)
// body.appendChild(ul)

// ul.append(li1, li2, li3) 
// ul.appendChild(li1, li2, li3) 

// 2-4. Delete
// removeChild
// ul.removeChild(li1) 
// ul.removeChild(li2)

// remove
// ul.remove()
// body.remove()

// 2-5. Element Styling
// li1.style.cursor = 'pointer'
// li2.style.color = 'blue'
// li3.style.background = 'red'

// setAttribute
// li3.setAttribute('id', 'king')

// getAttribute
// const getAttr = li1.getAttribute('style')
// const getAttr2 = li3.getAttribute('style')
// console.log(getAttr)
// console.log(getAttr2)