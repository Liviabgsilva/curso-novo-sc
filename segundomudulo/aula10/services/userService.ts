interface User {
  name: string;
  email: string;
}

export class UserService {
  private users: User[] = [
    { name: "Livia", email: "livia@example.com" },
    { name: "Aula", email: "aula@example.com" }
  ];

  // Retorna a lista de usuários em memória.
  getUsers() {
    return this.users;
  }

  // Adiciona um novo usuário na lista.
  addUser(user: User) {
    this.users.push(user);
  }
}
