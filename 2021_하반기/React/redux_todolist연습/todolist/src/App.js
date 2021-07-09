/* eslint-disable */

import logo from './logo.svg';
import './App.css';
import { createGlobalStyle } from 'styled-components';
import TodoTemplate from './components/TodoTemplate';
import TodoList from './components/TodoList';
import TodoCreate from './components/TodoCreate';


// createGlobalStyle이라는 스킬이 있길래 해봄!
// django로 치면 base.html 느낌같음
const GlobalStyle = createGlobalStyle`
  body {
    background: #e9ecef;
  }
`;

// GlobalStyle을 가장 바깥에 두고
// 컴포넌트 폴더를 따로 만든 후 다 import 해와서 구성했음
function App() {
  return (
    <div className="App">
      <GlobalStyle />
      <TodoTemplate>
        <TodoList />
        <TodoCreate />
      </TodoTemplate>
    </div>
  );
}

export default App;





