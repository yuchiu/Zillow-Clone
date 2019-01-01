const jayson = require("jayson");
const mongoose = require("mongoose");

const secrets = require("./utils/secrets");
const RPCInterface = require("./RPCInterface");

mongoose.connect(
  secrets.MONGODB_URI,
  { useNewUrlParser: true },
  err => {
    if (err) {
      console.log(`  DB Connection failed:${err}`);
    } else {
      console.log(
        `  DB Connection Success, connected to ${secrets.MONGODB_URI}`
      );
    }
  }
);

// create a server
const server = jayson.server(RPCInterface);

server
  .http()
  .listen(secrets.SERVICE_USER_PORT, () =>
    console.log(
      `  User Service listenning on port ${secrets.SERVICE_USER_PORT} in "${
        secrets.NODE_ENV
      }" mode`
    )
  );
