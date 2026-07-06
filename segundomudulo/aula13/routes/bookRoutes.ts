import { Router } from "express";
import { BookController } from "../controllers/bookController";

const router = Router();
const controller = new BookController();

// Lista livros cadastrados
router.get("/", controller.listBooks);

// Exibe formulário para novo livro
router.get("/create", controller.showCreateForm);

// Cria um livro
router.post("/create", controller.createBook);

// Exibe formulário para editar livro
router.get("/edit/:id", controller.showEditForm);

// Atualiza livro
router.post("/edit/:id", controller.updateBook);

// Exclui livro
router.post("/delete/:id", controller.deleteBook);

export { router as bookRouter };
