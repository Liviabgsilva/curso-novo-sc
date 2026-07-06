import { Request, Response } from "express";
import { ProductService } from "../services/productService";

export class ProductController {
  private productService = new ProductService();

  // Exibe a lista de produtos
  listProducts = (req: Request, res: Response) => {
    const products = this.productService.getProducts();
    res.render("products", { products });
  };

  // Exibe o formulário para criar novo produto
  showCreateForm = (req: Request, res: Response) => {
    res.render("productForm", { product: null, action: "/products/create", title: "Novo Produto" });
  };

  // Cria um produto e redireciona para a lista
  createProduct = (req: Request, res: Response) => {
    const { name, price } = req.body;
    this.productService.createProduct({ name, price: Number(price) });
    res.redirect("/products");
  };

  // Exibe o formulário de edição com dados preenchidos
  showEditForm = (req: Request, res: Response) => {
    const product = this.productService.getProductById(req.params.id);
    if (!product) {
      return res.status(404).send("Produto não encontrado");
    }
    res.render("productForm", { product, action: `/products/edit/${product.id}`, title: "Editar Produto" });
  };

  // Atualiza o produto existente
  updateProduct = (req: Request, res: Response) => {
    const { name, price } = req.body;
    this.productService.updateProduct(req.params.id, { name, price: Number(price) });
    res.redirect("/products");
  };

  // Remove produto
  deleteProduct = (req: Request, res: Response) => {
    this.productService.deleteProduct(req.params.id);
    res.redirect("/products");
  };
}
