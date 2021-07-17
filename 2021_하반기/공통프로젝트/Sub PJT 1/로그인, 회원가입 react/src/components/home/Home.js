import React, { useState, useEffect } from 'react';
import "./Home.css"
import { Button } from 'react-bootstrap'
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux'

// import store from "../index.js"


function Home() {

  const [authUserLocal, setAuthUserLocal] = useState(true);
  useEffect(()=> {
    const localToken = localStorage.getItem('token')
    if (localToken) {
      setAuthUserLocal(false)
    }
    console.log('컴포넌트가 화면에 나타남')
    return () => {
      setAuthUserLocal(true)
      console.log('컴포넌트가 화면에서 사라짐')
    }
  })

  return (
    <div>
      <div className="jumbo"></div>
      <h2>Hi Hi ~ 안녕하세요!</h2>
      <br/>
      { 
        authUserLocal
        ?
        <div>
          <Link to="login">
            <Button variant="info" size="lg">Login</Button>
          </Link>
        </div>
        : null
      }
 
    </div>

  )
}


export default Home;