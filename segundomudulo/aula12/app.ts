import express from "express";
import path from "path";
import { productRouter } from "./routes/productRoutes";

const app = express();

// Configuração básica do Express e do Pug
app.set("view engine", "pug");
app.set("views", path.join(process.cwd(), "segundomudulo", "aula12", "views"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rota principal para produtos com CRUD completo
app.use("/products", productRouter);

app.listen(3000, () => {
  console.log("Servidor Aula 12 rodando em http://localhost:3000/products");
});
