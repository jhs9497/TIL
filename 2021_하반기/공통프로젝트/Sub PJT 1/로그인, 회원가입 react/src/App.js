/* eslint-disable */
import React, { useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import { createGlobalStyle } from 'styled-components';
import TodoTemplate from './components/TodoTemplate';
import TodoList from './components/TodoList';
import TodoCreate from './components/TodoCreate';

import Signup from './components/signup/Signup'
import Home from './components/home/Home'
import Login from './components/login/Login'

import { Link, Route, Router } from 'react-router-dom';

import { ButtonGroup, Button } from 'react-bootstrap';
import { useHistory } from 'react-router-dom';
import { useSelector } from "react-redux";
import { useDispatch } from 'react-redux';
import { useState } from 'react';


// createGlobalStyle이라는 스킬이 있길래 해봄!
// django로 치면 base.html 느낌같음
const GlobalStyle = createGlobalStyle`
  body {
    background : lightblue;
`;

const GlobalStyle2 = createGlobalStyle`
  body {
    background: lightskyblue;
  }
`

// GlobalStyle을 가장 바깥에 두고
// 컴포넌트 폴더를 따로 만든 후 다 import 해와서 구성했음
function App() {
  // const auth = localStorage.getItem('token')
  const history = useHistory()
  const dispatch = useDispatch()
  const authUser = useSelector(state => state.authUserReducer)

  // const [로컬로그인, 로컬로그인변경] = useState(false);

  // useEffect(() => {
  //   const local = localStorage.getItem('token')
  //   if(local) {
  //     로컬로그인변경(true)
  //   }
  // }, [])

  function Logout() {
    localStorage.clear() 
    history.push('home')
    dispatch({ type : 'LOGOUT' })
    setAuth(false)
  }


  const [auth, setAuth] = useState(false);
  useEffect(()=> {
    const 로컬 = localStorage.getItem('token')
    if (로컬) {
      setAuth(true)
    }
  })

  return (
    
    <div className="App">

      {
        auth
        ?
        <div className="navbar">
          <ButtonGroup aria-label="Basic example">
            <Link to='./home'>
              <Button variant="success">Home</Button>
            </Link>
            <Link to='./todolist'>
              <Button variant="success">TodoList</Button>
            </Link>
            <Button 
              variant="success"
              onClick={Logout}
            >LOGOUT
            </Button>
          </ButtonGroup>
        </div>
        : null
      }



      <Route exact path="/home">
        <Home />
      </Route>

      <Route exact path="/login">
        <GlobalStyle2 />
        <Login />
      </Route>

      <Route exact path="/signup">
        <GlobalStyle2 />
        <Signup />
      </Route>


      <Route exact path="/todolist">
        <GlobalStyle />
        <TodoTemplate>
          <TodoList />
          <TodoCreate />
        </TodoTemplate>
      </Route>
    </div>
  );
}

export default App;





