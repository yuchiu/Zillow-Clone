import jayson from "jayson";
import {
  SERVICE_USER_HOST,
  SERVICE_USER_PORT,
  SERVICE_PROPERTY_HOST,
  SERVICE_PROPERTY_PORT
} from "./secrets";

// create a rpc client

export const userService = jayson.client.http({
  hostname: SERVICE_USER_HOST,
  port: SERVICE_USER_PORT
});

export const realEstateService = jayson.client.http({
  hostname: SERVICE_PROPERTY_HOST,
  port: SERVICE_PROPERTY_PORT
});
