import { Request, Response } from "express";
import { UserService } from "../services/userService";

export class UserController {
  private service = new UserService();

  // A lista de usuários é solicitada da camada de serviço e enviada para a view.
  listUsers = (req: Request, res: Response) => {
    const users = this.service.getUsers();
    res.render("users", { users });
  };

  // A criação de usuário delega ao serviço e depois redireciona para exibir a lista.
  createUser = (req: Request, res: Response) => {
    const { name, email } = req.body;
    this.service.addUser({ name, email });
    res.redirect("/users");
  };
}
