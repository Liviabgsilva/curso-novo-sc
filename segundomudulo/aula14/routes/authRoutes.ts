import { Router } from "express";
import { AuthController } from "../controllers/authController";

const router = Router();
const controller = new AuthController();

// Rota de cadastro
router.post("/register", controller.register);

// Rota de login
router.post("/login", controller.login);

export { router as authRouter };
