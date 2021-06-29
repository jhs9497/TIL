import logo from './logo.svg';
import './App.css';

function App() {

  let posts = '강남 고기 맛집';
  function 함수 (){
    return 100
  }

  return (
    <div className="App">
      <div className="black-nav">
        <div style={ { color : 'blue', fontSize : '30px' } }>개발 Blog</div>
      </div>
      <div className='list'>
        <h3>{ posts }</h3>
        <p>2월 17일 발행</p>
        <hr/>
      </div>
    </div>
  );
}

export default App;
