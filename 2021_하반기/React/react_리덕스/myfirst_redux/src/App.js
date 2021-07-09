import './App.css';
import {useSelector, useDispatch} from 'react-redux';
import {decrement, increment} from './actions'

function App() {
  const counter = useSelector(state => state.counter);
  const isLogged = useSelector(state => state.isLogged);
  const dispatch = useDispatch();

  return (
    <div className="App">
      <h1>hello</h1>
      <h1>Counter {counter}</h1>
      <button onClick={() => dispatch(increment(5))}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button>
      {
        isLogged ? <h3>Valuable Information I should'n see</h3>
        : null
      }
      
    </div>
  );
}

export default App;
