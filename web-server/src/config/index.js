export default {
  PORT: 3030,
  KEY: {
    JWT_SECRET: "djiosajdi9r8je9r09321309r092fdsadsaasd1disjvbmi08"
  },
  MONGO_DB: {
    MONGO_LOCAL_URI:
      process.env.MONGO_LOCAL_URI || "mongodb://localhost:27017/node-server",
    MONGO_CLOUD_URI:
      process.env.MONGO_CLOUD_URI ||
      "mongodb://admin01:admin01@ds145072.mlab.com:45072/node-server"
  }
};
