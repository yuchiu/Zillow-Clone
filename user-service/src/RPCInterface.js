const controller = require("./controllers");

// create a server{
module.exports = {
  authenticateJWT(credentials, callback) {
    controller.authenticateJWT(credentials, callback);
  },
  signUpUser(credentials, callback) {
    controller.signUpUser(credentials, callback);
  },
  signInUser(credentials, callback) {
    controller.signInUser(credentials, callback);
  },
  tryAutoSignIn(user, callback) {
    controller.tryAutoSignIn(user, callback);
  }
};
