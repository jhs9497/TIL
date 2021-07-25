import React from 'react';
import logo from './logo.svg';
import './App.css';
import './index.css';

function App() {
  const name = { name: '조현식' };
  console.log(name);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>항 하이 하 이루</div>
        <div>하이항 하이 하이 ㅁㄴㄻㅇㄴㄹ</div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
