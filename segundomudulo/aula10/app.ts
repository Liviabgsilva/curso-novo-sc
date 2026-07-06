import express from "express";
import path from "path";
import { userRouter } from "./routes/userRoutes";

const app = express();

// Configuração do template engine Pug.
app.set("view engine", "pug");
app.set("views", path.join(process.cwd(), "segundomudulo", "aula10", "views"));

// Middleware para entender JSON e dados de formulário.
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rota principal delegada ao módulo de rotas.
app.use("/users", userRouter);

app.listen(3000, () => {
  console.log("Servidor Aula 10 rodando em http://localhost:3000/users");
});
