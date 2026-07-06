interface Book {
  id: string;
  title: string;
  author: string;
  price: number;
}

export class BookService {
  private books: Book[] = [
    { id: "1", title: "Introdução a Node.js", author: "Autor A", price: 29.9 },
    { id: "2", title: "Aprendendo Express", author: "Autor B", price: 39.9 }
  ];

  // Retorna todos os livros cadastrados.
  getBooks() {
    return this.books;
  }

  // Cria um novo livro e adiciona à lista.
  createBook(book: Omit<Book, "id">) {
    const newBook = { id: String(Date.now()), ...book };
    this.books.push(newBook);
    return newBook;
  }

  // Busca livro pelo ID.
  getBookById(id: string) {
    return this.books.find((book) => book.id === id);
  }

  // Atualiza os dados de um livro existente.
  updateBook(id: string, update: Omit<Book, "id">) {
    const index = this.books.findIndex((book) => book.id === id);
    if (index < 0) return null;
    this.books[index] = { id, ...update };
    return this.books[index];
  }

  // Remove o livro da lista.
  deleteBook(id: string) {
    this.books = this.books.filter((book) => book.id !== id);
  }
}
