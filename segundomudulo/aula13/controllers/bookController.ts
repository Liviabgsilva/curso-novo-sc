import { Request, Response } from "express";
import { BookService } from "../services/bookService";

export class BookController {
  private bookService = new BookService();

  // Exibe a lista de livros.
  listBooks = (req: Request, res: Response) => {
    const books = this.bookService.getBooks();
    res.render("books", { books });
  };

  // Exibe o formulário de criação.
  showCreateForm = (req: Request, res: Response) => {
    res.render("bookForm", { book: null, action: "/books/create", title: "Novo Livro" });
  };

  // Cria um novo livro e redireciona para a lista.
  createBook = (req: Request, res: Response) => {
    const { title, author, price } = req.body;
    this.bookService.createBook({ title, author, price: Number(price) });
    res.redirect("/books");
  };

  // Exibe formulário para edição com dados preenchidos.
  showEditForm = (req: Request, res: Response) => {
    const book = this.bookService.getBookById(req.params.id);
    if (!book) {
      return res.status(404).send("Livro não encontrado");
    }
    res.render("bookForm", { book, action: `/books/edit/${book.id}`, title: "Editar Livro" });
  };

  // Atualiza o livro existente.
  updateBook = (req: Request, res: Response) => {
    const { title, author, price } = req.body;
    this.bookService.updateBook(req.params.id, { title, author, price: Number(price) });
    res.redirect("/books");
  };

  // Exclui o livro.
  deleteBook = (req: Request, res: Response) => {
    this.bookService.deleteBook(req.params.id);
    res.redirect("/books");
  };
}
