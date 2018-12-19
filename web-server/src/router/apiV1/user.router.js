import express from "express";

import { userController } from "../../controllers";
import authenticate from "../../middlewares/authenticate";

const router = express.Router();

router.get("/auth", authenticate, userController.tryAutoSignIn);
router.post("/signup", userController.signUpUser);
router.post("/signin", userController.signInUser);

export default router;
