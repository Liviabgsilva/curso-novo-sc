interface Product {
  id: string;
  name: string;
  price: number;
}

export class ProductService {
  private products: Product[] = [
    { id: "1", name: "Caneta", price: 3.5 },
    { id: "2", name: "Caderno", price: 12.9 }
  ];

  // Retorna todos os produtos cadastrados.
  getProducts() {
    return this.products;
  }

  // Cria um novo produto na lista em memória.
  createProduct(product: Omit<Product, "id">) {
    const newProduct = { id: String(Date.now()), ...product };
    this.products.push(newProduct);
    return newProduct;
  }

  // Busca produto por ID.
  getProductById(id: string) {
    return this.products.find((product) => product.id === id);
  }

  // Atualiza produto existente.
  updateProduct(id: string, update: Omit<Product, "id">) {
    const index = this.products.findIndex((product) => product.id === id);
    if (index < 0) return null;
    this.products[index] = { id, ...update };
    return this.products[index];
  }

  // Exclui produto e retorna a lista atualizada.
  deleteProduct(id: string) {
    this.products = this.products.filter((product) => product.id !== id);
  }
}
