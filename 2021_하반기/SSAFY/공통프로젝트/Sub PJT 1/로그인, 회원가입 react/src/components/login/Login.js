import React from 'react';
import './Login.css'
import { Form, Button, Container } from 'react-bootstrap'
import { Link } from 'react-router-dom';
import axios from 'axios';
import { useDispatch } from 'react-redux';
import { useState } from 'react';
import { useHistory } from 'react-router-dom';



function Login() {

  const history = useHistory();
  const dispatch = useDispatch();


  const [로그인정보, 로그인정보변경] = useState([
    {
      username : '',
      password: '',
    }
  ])

  const logininfoChange = e => {
    const { name, value } = e.target;
    로그인정보변경({
      ...로그인정보,
      [name]: value
    })
  }

  // 로그인 axios 요청 보내기
  async function tryLogin(e) {
    e.preventDefault();

    const data = 로그인정보
    const LOGIN_URL = '/auth/login'


    await axios.post(LOGIN_URL, data)
    .then((res) => {
      const token = '로그인됨!'
      dispatch({ type : 'LOGIN' })
      window.localStorage.setItem('token', token)
      window.localStorage.setItem('username', data.username)

      history.push('home')
      dispatch({ type : 'SIGNUP', payload : data })
    })
    .catch((err) => {
      console.log(err)
      alert('아이디나 비밀번호를 확인해라')
    })
  }


  return (
    <div className="jumbo2">
      <div className="Xbutton">
        <Link to="home" >
          <Button variant="danger" type="submit">
            X
          </Button>
        </Link>
      </div>
      <h1>Login</h1>
      <Container>
        <Form>
          <Form.Group className="mb-3" controlId="formBasicID">
            <Form.Label>ID</Form.Label>
            <Form.Control 
              type="text" 
              placeholder="Enter ID" 
              name="username"
              onChange={logininfoChange}
            />
            <Form.Text className="text-muted">
            </Form.Text>
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control 
              type="password" 
              placeholder="Password" 
              name="password"
              onChange={logininfoChange}
            />
          </Form.Group>

          <Button 
            variant="primary"
            size="lg"
            onClick={tryLogin}
          >
            Login
          </Button>
          <div>
            <h5>ID가 없으신가요 ?</h5>
            <Link to="signup">
              <Button variant="secondary">Sign up</Button>
            </Link>
          </div>

        </Form>
      </Container>
    </div>
  )
}

export default Login;