import { Router } from "express";
import { ProductController } from "../controllers/productController";

const router = Router();
const controller = new ProductController();

// Rota para mostrar todos os produtos
router.get("/", controller.listProducts);

// Rota para exibir o formulário de criação
router.get("/create", controller.showCreateForm);

// Rota para cadastrar um novo produto
router.post("/create", controller.createProduct);

// Rota para exibir o formulário de edição
router.get("/edit/:id", controller.showEditForm);

// Rota para atualizar um produto existente
router.post("/edit/:id", controller.updateProduct);

// Rota para excluir produto
router.post("/delete/:id", controller.deleteProduct);

export { router as productRouter };
