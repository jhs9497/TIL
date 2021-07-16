import React from 'react'

const Book = (props) => {
  const { img, title, author } = props.book;
  
  const clickHandler = () => {
    alert('hello world')
  };

  const name = 'Johyusik'
  return <article className='book'>
    <img 
      src={img}
      alt="" 
    />
    <h1 onClick={() => alert('하하')}>내가 고른 책은</h1>
    <h4>{title}</h4>
    <h5>{author}</h5>
    <h3>my name : {name.toUpperCase()}</h3>
    <button type="button" onClick={clickHandler}>하이하이</button>

  </article>
};

const Title = () => {
  return <h1>코딩진로</h1>
}

const Author = () => {
  return <h4 style={{color:'#617d98', fontSize: '0.75rem'}}>류채윤</h4>
}


export default Book