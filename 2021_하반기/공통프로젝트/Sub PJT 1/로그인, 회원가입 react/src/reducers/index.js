import { combineReducers } from "redux";
import createReducer from "./create.js";
import alertReducer from "./alert.js";
import userReducer from "./user.js"
import authUserReducer from "./authUser.js"

const allReducers = combineReducers({
  createReducer,
  alertReducer,
  userReducer,
  authUserReducer,
})
export default allReducers;