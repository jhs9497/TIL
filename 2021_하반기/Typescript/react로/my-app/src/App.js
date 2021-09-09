"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
require("./App.css");
let 박스 = <div>asdfasdf</div>;
// HTML을 변수에 담을 때
function App() {
    let [user, setUser] = (0, react_1.useState)('kim');
    // useState할 때는 useState안에 있는 type을 기준으로 자동으로 type지정 됨!
    let [굳이, set굳이] = (0, react_1.useState)('jo');
    // 근데 굳이 초기에 넣어준 type외에 다른 것도 받을 수 있게 하고 싶으면 이렇게 타입을 넣어주면됨!
    return (<div>
      {박스}
      <h4>안녕하십니까</h4>
      <Profile name="철수"/>
    </div>);
}
// props로 받는 친구는 항상 object로 넘어옴 그러므로 object 타입지정을 해줘야함
function Profile(props) {
    return (<div>
      프로필입니다.
      {props.name}입니다
    </div>);
}
exports.default = App;
