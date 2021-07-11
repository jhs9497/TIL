import React from 'react';
import { Form, Container } from 'react-bootstrap'
import { Link } from 'react-router-dom';

function Login() {
  return(
    <Container>
      <Form>
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control type="email" placeholder="Enter email" />
          <Form.Text className="text-muted">
            We'll never share your email with anyone else.
          </Form.Text>
        </Form.Group>

        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" placeholder="Password" />
        </Form.Group>
        <button>
          <Link to="/todolist">
            Submit
          </Link>
        </button>
      </Form>
    </Container>
  )
}

export default Login;