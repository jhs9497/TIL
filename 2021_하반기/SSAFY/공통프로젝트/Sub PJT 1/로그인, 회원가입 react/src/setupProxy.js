// const { createProxyMiddleware } = require('http-proxy-middleware');
// module.exports = function(app) {
//   app.use(
//     '/accounts/signin', 
//     createProxyMiddleware({
//       target: 'http://localhost:8000',
//       changeOrigin: true,
//     })
//   );
// };


const proxy = require('http-proxy-middleware');
module.exports = function(app) {
  app.use(
    proxy('/accounts/signin', {
      target: 'http://localhost:8000',
      changeOrigin: true,
    })
  );
  app.use(
    proxy('/auth/login', {
      target: 'http://localhost:8000',
      changeOrigin: true,
    })
  );
};