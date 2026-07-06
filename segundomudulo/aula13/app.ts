import express from "express";
import path from "path";
import { bookRouter } from "./routes/bookRoutes";

const app = express();

// Configuração da view engine Pug.
app.set("view engine", "pug");
app.set("views", path.join(process.cwd(), "segundomudulo", "aula13", "views"));

// Middlewares para dados JSON e formulários.
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Todas as rotas de CRUD estão isoladas neste módulo.
app.use("/books", bookRouter);

app.listen(3000, () => {
  console.log("Servidor Aula 13 rodando em http://localhost:3000/books");
});
