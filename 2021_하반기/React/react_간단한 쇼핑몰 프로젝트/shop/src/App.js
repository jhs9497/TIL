/* eslint-disable */
import logo from './logo.svg';
import React, {useState} from 'react';
import { Navbar,Container,Nav,NavDropdown,Button } from 'react-bootstrap';
import './App.css';
import Data from './data.js';
import Detail from './Detail.js';
import axios from 'axios';

import { Link, Route, Switch } from 'react-router-dom';

function App() {

  let [shoes, shoes변경] = useState(Data);
  let [재고 , 재고변경] = useState([10,11,12])

  return (
    <div className="App">
      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="#home">ShoeShop</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link><Link to="/">Home</Link></Nav.Link>
              <Nav.Link><Link to="/detail">Detail</Link></Nav.Link>
              <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      
      <Switch>
      
        <Route exact path="/">
          <div className="jumbo">
            <h1>20% Season Off</h1>
            <p>
              블라블라
            </p>
              <Button varinant="primary">Leanr more</Button>
          </div>
          <div className="container">
            <div className="row">
              {
                shoes.map(function(value, i){
                  return <ShoesInfo shoes={shoes[i]} i={i} key={i}/>
                })
              }
            </div>
            <button className="btn btn-primary" onClick={()=>{

              // 서버 URL로 내 데이터 전달할때
              // axios.post('서버URL', { id : 'asdfasdf', pw : 1234})
              // .then()
              // .catch()

              // 로딩중이라는 UI 띄우기
              

              axios.get('https://codingapple1.github.io/shop/data2.json') // 새로고침없이 데이터 가져올수 있음      
              .then((result)=>{
                // 로딩중이라는 UI 안보이게 처리
                shoes변경( [...shoes, ...result.data] ); // ...하면 대괄호 벗겨줘란 뜻! 벗기고 또 []안에 묶었으니 일종의 스킬?
              })        
              .catch(()=>{
                
              })

            }}>더보기</button>
          </div>
        </Route>



        <Route path="/detail/:id">
          <Detail shoes={shoes} 재고={재고} 재고변경={재고변경}/>
        </Route>
        {/* <Route path="/어쩌구" component={Modal}></Route> 이것도 가능! */}

        <Route path="/:id"> 
          <div>아무거나 적었을 때 이거 보여주셈</div>
        </Route>

      </Switch>
            
    </div>
  );
}

function ShoesInfo (props) {
  return (
    <div className="col-md-4">
      <img src={ 'https://codingapple1.github.io/shop/shoes' + (props.i + 1) + '.jpg' } width="100%" />
      <h4>{ props.shoes.title }</h4>
      <p>{ props.shoes.content }</p>
      <p>{ props.shoes.price }원</p>
    </div> 
  )
}

export default App;

