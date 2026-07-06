import express from "express";
import path from "path";

const app = express();

app.set("view engine", "pug");
app.set("views", path.join(process.cwd(), "segundomudulo", "aula9"));

app.get("/", (req, res) => {
  res.render("index", {
    usuario: { nome: "Livia" },
    lista: ["Item A", "Item B", "Item C"]
  });
});

app.listen(3000, () => {
  console.log("Servidor Aula 9 criado em http://localhost:3000");
});
