const produtos = [
    { id: 1, nome: "Camiseta", preco: 25.99 },
    { id: 2, nome: "Calça", preco: 39.99 },
    { id: 3, nome: "Tênis", preco: 299.90 },
];

const produtosJson = JSON.stringify(produtos);
console.log(produtos);
console.log(produtosJson);

const produtosObj = JSON.parse(produtosJson);
console.log(produtosObj);