import { Request, Response, NextFunction } from "express";
import { AuthService } from "../services/authService";

export class AuthController {
  private authService = new AuthService();

  // Registro de usuário.
  register = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const { email, password } = req.body;
      const user = await this.authService.register(email, password);
      res.status(201).json({ message: "Usuário criado", user });
    } catch (error) {
      next(error);
    }
  };

  // Login de usuário.
  login = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const { email, password } = req.body;
      const token = await this.authService.login(email, password);
      res.json({ token });
    } catch (error) {
      next(error);
    }
  };
}
