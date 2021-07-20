/* eslint-disable */
import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { createGlobalStyle } from 'styled-components';

import TodoTemplate from './components/todo/TodoTemplate';
import TodoList from './components/todo/TodoList';
import TodoCreate from './components/todo/TodoCreate';

import Signup from './components/signup/Signup'
import Home from './components/home/Home'
import Login from './components/login/Login'

import { Link, Route } from 'react-router-dom';

import { ButtonGroup, Button } from 'react-bootstrap';

import { useHistory } from 'react-router-dom';
import { useSelector } from "react-redux";
import { useDispatch } from 'react-redux';


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
  const history = useHistory()
  const dispatch = useDispatch()
  const authUserRedux = useSelector(state => state.authUserReducer)

  function Logout() {
    localStorage.clear() 
    history.push('home')
    dispatch({ type : 'LOGOUT' })
    setAuthUserLocal(false)
  }


  const [authUserLocal, setAuthUserLocal] = useState(false);
  useEffect(()=> {
    const localToken = localStorage.getItem('token')
    if (localToken) {
      setAuthUserLocal(true)
    }
  })

  return (
    
    <div className="App">

      {/* 어느 페이지에서나 보이는 곳! Navbar같은 */}

      {
        authUserLocal
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

      


      {/* 라우터 및 그에 따른 컴포넌트 설정*/}

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





