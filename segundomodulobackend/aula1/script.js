
class Moto {
    constructor(fabricante, modelo, ano, ){
        this.fabricante = fabricante; // Propriedade da Classe
        this.modelo = modelo; // Propriedade da Classe
        this.ano = ano; // Propriedade da Classe
       
    }

      mostrarDadosDaMoto()
    {
        console.log(`${this.fabricante} ${this.modelo}, ${this.ano}  `)
    }

    mostrarModelo(){
        console.log(`O modelo da moto é ${this.modelo}`);
    }

    acelerar(){
        console.log("Acelerando...");
    }
}
class Carro {
    constructor(fabricante, modelo, ano, tipo, qtdPortas){
        this.fabricante = fabricante; // Propriedade da Classe
        this.modelo = modelo; // Propriedade da Classe
        this.ano = ano; // Propriedade da Classe
        this.tipo = tipo; // Propriedade da Classe
        this.qtdPortas = qtdPortas; // Propriedade da Classe
    }

    mostrarDadosDoCarro()
    {
        console.log(`${this.fabricante} ${this.modelo}, ${this.ano} (${this.tipo}), ${this.qtdPortas} portas `)
    }

    mostrarModelo(){
        console.log(`O modelo do carro é ${this.modelo}`);
    }

    acelerar(){
        console.log("Acelerando...");
    }
}

const meuCarro = new Carro("Ford","KA","2008","Sedan",4);
const minhaMoto = new Moto("yamaha", "k2", "2008");
minhaMoto.mostrarDadosDaMoto();
meuCarro.mostrarDadosDoCarro();