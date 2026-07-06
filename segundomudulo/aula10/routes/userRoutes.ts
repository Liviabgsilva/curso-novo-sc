import { Router } from "express";
import { UserController } from "../controllers/userController";

const router = Router();
const userController = new UserController();

// Rota de exibição de lista de usuários.
router.get("/", userController.listUsers);

// Rota de criação de usuário.
router.post("/create", userController.createUser);

export { router as userRouter };
