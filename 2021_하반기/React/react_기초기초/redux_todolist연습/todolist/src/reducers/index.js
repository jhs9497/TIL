import { combineReducers } from "redux";
import createReducer from "./create.js";
import alertReducer from "./alert.js";

const allReducers = combineReducers({
  createReducer,
  alertReducer
})
export default allReducers;