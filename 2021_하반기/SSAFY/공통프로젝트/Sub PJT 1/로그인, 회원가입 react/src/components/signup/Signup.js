import './Signup.css'
import React, { useState } from 'react';
import { Form, Button, Container } from 'react-bootstrap'
import { Link } from 'react-router-dom';
import axios from 'axios';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';


function Signup() {

  const history = useHistory();
  const dispatch = useDispatch();

  const [유저정보, 유저정보변경] = useState([
    {
      username : '',
      password: '',
      password_confirmation: '',
      name: '',
      email:'',
    }
  ]) 

  // input값에 적은 유저정보 저장하기 
  const userinfoChange = e =>{
    const { name, value } = e.target;
    유저정보변경({
      ...유저정보,
      [name]: value
    });
  };

  // SignupOK하면 자동 로그인 실행
  function autoLogin(data) {
    // console.log(data.username)
    const LOGIN_URL = 'auth/login'
    const userinfo = {
      username : data.username,
      password : data.password,
    }
    axios.post(LOGIN_URL, userinfo)
    .then((res) => {
      const token = '로그인됨!'

      window.localStorage.setItem('token', token)
      dispatch({ type : 'LOGIN' })
      window.localStorage.setItem('username', data.username)
      history.push('home')
    })
    .catch((err) => {
      console.log(err)
    })

    dispatch({ type : 'SIGNUP', payload : data })
  }


  // 회원가입 axios 요청 보내기
  function userCreate() {
    const data = 유저정보
    // https://cors-anywhere.herokuapp.com/
    const USER_CREATE_URL = 'accounts/signin'

    axios.post(USER_CREATE_URL, data)
    .then(function(res) {
      // 회원가입 잘 된 유저정보 redux에 저장하는 함수
      autoLogin(data)
    })
    .catch(function(err) {
      console.log(err)
      alert('뭔가가 잘못됐음 ID 중복이거나! 입력하라는거 제대로 입력안했거나!')
    })
  }



  return (
    <div className="jumbo3">
      
      <div className="Xbutton">
        <Link to="login" >
          <Button variant="danger" type="submit">
            X
          </Button>
        </Link>
      </div>
      <h1>Sign Up</h1>
      <Container>
        <Form>
          <Form.Group className="mb-3" controlId="formBasicID">
            <Form.Control 
              type="text" 
              placeholder="ID"
              name="username"
              onChange={userinfoChange}
            />
            <Form.Text className="text-muted">
            </Form.Text>
          </Form.Group>

          <br />

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Control 
              type="password" 
              placeholder="Password"
              name="password"
              onChange={userinfoChange} 
            />
          </Form.Group>

          <br />

          <Form.Group className="mb-3" controlId="formBasicPassword_Confirmation">
            <Form.Control 
              type="password" 
              placeholder="Password Confirmation" 
              name="password_confirmation"
              onChange={userinfoChange}
            />
            {
              유저정보.password !== 유저정보.password_confirmation
              ? <p>비밀번호 맞춰주소</p>
              : null
            }

          </Form.Group>
  

          <br />

          <Form.Group className="mb-3" controlId="formBasicName">
            <Form.Control 
              type="text" 
              placeholder="Name" 
              name="name"
              onChange={userinfoChange}
            />
            <Form.Text className="text-muted">
            </Form.Text>
          </Form.Group>

          <br />

          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Control 
              type="email" 
              placeholder="email" 
              name="email"
              onChange={userinfoChange}
            />
            <Form.Text className="text-muted">
            </Form.Text>
          </Form.Group>

          <br />

          <Button 
            variant="primary" 
            onClick={userCreate}
            size="lg"
          >
            SignUp
          </Button>

        </Form>
      </Container>
    </div>
  )
}


export default Signup;