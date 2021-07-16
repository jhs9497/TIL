import React from 'react';
import "./Home.css"
import { Button } from 'react-bootstrap'
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux'

// import store from "../index.js"


function Home() {

  const authUser = useSelector(state => state.authUserReducer.로그인)
  const auth = localStorage.getItem('token')

  return (
    <div>
      <div className="jumbo"></div>
      <h2>Hi Hi ~ 안녕하세요!</h2>
      <br/>
      {
        !auth
        ?
        <div>
          <Link to="login">
            <Button variant="info" size="lg">Login</Button>
          </Link>
        </div>
        : null
      }

      {
        authUser === 'O'
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