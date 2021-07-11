/* eslint-disable */

import logo from './logo.svg';
import './App.css';
import { createGlobalStyle } from 'styled-components';
import TodoTemplate from './components/TodoTemplate';
import TodoList from './components/TodoList';
import TodoCreate from './components/TodoCreate';

import Home from './components/home/Home'
import Login from './components/login/Login'

import { Link, Route } from 'react-router-dom';

import { Navbar,Container,Nav,NavDropdown,Button } from 'react-bootstrap';


// createGlobalStyle이라는 스킬이 있길래 해봄!
// django로 치면 base.html 느낌같음
const GlobalStyle = createGlobalStyle`
  body {
    background: #e9ecef;
  }
`;

// 라우터 설정


// GlobalStyle을 가장 바깥에 두고
// 컴포넌트 폴더를 따로 만든 후 다 import 해와서 구성했음
function App() {
  return (
    <div className="App">

      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="#home">뭐하지</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link><Link to="/">Home</Link></Nav.Link>
              <Nav.Link><Link to="/todolist">Todolist</Link></Nav.Link>
              <Nav.Link><Link to="/login">Login</Link></Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <Route exact path="/">
        <Home/>
      </Route>

      <Route exact path="/login">
        <div>로그인페이지입니다</div>
        <Login/>
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





