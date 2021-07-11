import React from 'react';
import "./Home.css"
import { Button } from 'react-bootstrap'
import { Link } from 'react-router-dom';
  
  
function Home() {
  return (
    <div className="jumbo">오늘뭐하지 ?
      <Button><Link to="login">로그인</Link></Button>
      <Button>로그인</Button>
      <button><Link to="login">로그인</Link></button>
    </div>
  )
}


export default Home;