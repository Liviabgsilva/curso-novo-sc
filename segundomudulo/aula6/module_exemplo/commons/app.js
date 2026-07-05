var pessoa = require("./commons/pessoa");
var soma = require("./commons/soma");
var imposto = require("./commons/calculoimposto")
livia = pessoa();

//console.log(JSON.stringify(livia));
//console.log(soma(2,2));

console.log('Valor do produto com imposto: ' + imposto.adicionar(10));
console.log('Valor do imposto:' + imposto.valor(10));
console.log('Taxa do Imposto:' + imposto.taxa)