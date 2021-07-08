import React from 'react'
import ReactDom from 'react-dom'

// CSS
import './index.css'

// 2가지의 import, export 방법
import {books} from './books.js'
import Book from './book.js'



const names = ['john', 'peter', 'susan'];

const newName = names.map((name) =>{
  return <h1>{name}</h1>
})

function BookList(){

  return (
    <section className="booklist">
      {books.map((book) => {

        return (
          <Book key={book.id} book={book}/>
        )
      })}
    </section>
  );
}



ReactDom.render(<BookList/>, document.getElementById('root'));
// Greeting이라는 컴포넌트를 index.hmtl에 root로 보내는 멍령어