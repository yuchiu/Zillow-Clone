import express from "express";

import { userController } from "../../controllers";
import authenticateJWT from "../../middlewares/authenticateJWT";

const router = express.Router();

router.get("/auth", authenticateJWT, userController.tryAutoSignIn);
router.post("/signup", userController.signUpUser);
router.post("/signin", userController.signInUser);

export default router;
