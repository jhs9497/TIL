import { combineReducers } from "redux";
import createReducer from "./create.js";
import alertReducer from "./alert.js";
import userReducer from "./userinfo.js"
import authUserReducer from "./authUser.js"

const allReducers = combineReducers({
  createReducer,
  alertReducer,
  userReducer,
  authUserReducer,
})
export default allReducers;