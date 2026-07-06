import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";

interface User {
  id: string;
  email: string;
  passwordHash: string;
}

const JWT_SECRET = "secret-key"; // Em produção, use variáveis de ambiente.

export class AuthService {
  private users: User[] = [];

  // Cria usuário com senha criptografada.
  async register(email: string, password: string) {
    if (this.users.find((user) => user.email === email)) {
      throw new Error("Usuário já existe");
    }

    const passwordHash = await bcrypt.hash(password, 8);
    const user = { id: String(Date.now()), email, passwordHash };
    this.users.push(user);
    return { id: user.id, email: user.email };
  }

  // Valida credenciais e retorna token JWT.
  async login(email: string, password: string) {
    const user = this.users.find((u) => u.email === email);
    if (!user) {
      throw new Error("Usuário ou senha inválidos");
    }

    const valid = await bcrypt.compare(password, user.passwordHash);
    if (!valid) {
      throw new Error("Usuário ou senha inválidos");
    }

    const token = jwt.sign({ userId: user.id }, JWT_SECRET, { expiresIn: "1h" });
    return token;
  }
}
