## React Persist

출처 : https://kyounghwan01.github.io/blog/React/redux/redux-persist/#%E1%84%89%E1%85%A9%E1%84%80%E1%85%A2-%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB-%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%B2



```react
yarn add redux-persist
```



```react
// reducers/index.js
import { persistReducer } from "redux-persist";
import storage from "redux-persist/lib/storage";

const persistConfig = {
  key: "root",
  // localStorage에 저장합니다.
  storage,
  // auth, board, studio 3개의 reducer 중에 auth reducer만 localstorage에 저장합니다.
  whitelist: ["auth"]
  // blacklist -> 그것만 제외합니다
};

export default persistReducer(persistConfig, rootReducer);
```



```react
// src/index.js
import { persistStore } from "redux-persist";
import { PersistGate } from "redux-persist/integration/react";

const persistor = persistStore(store);

const Root = () => (
  <Provider store={store}>
    <PersistGate loading={null} persistor={persistor}>
      <App />
    </PersistGate>
  </Provider>
);
```

