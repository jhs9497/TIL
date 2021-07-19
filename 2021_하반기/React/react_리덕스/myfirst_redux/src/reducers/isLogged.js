const loggedReducer = (state = false, actioin) => {
  switch(actioin.type){
    case 'SIGN_IN':
      return !state;
    default:
      return state;
  }
};
export default loggedReducer;