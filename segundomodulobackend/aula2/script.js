console.log("inicio de execucao");
function buscaDadosDoServidor() {
    // CODIGO QUE BUSCA DADOS DO SERVIDOR
    return new Promise((resolve, reject) => {
        console.log("Buscando dados no servidor");

        setTimeout(() => {
            let sucesso = Math.random() > 0.5;

            if (sucesso) {
                resolve("Dados recebidos com sucesso");
            } else {
                reject("falha ao buscar dados do serviodr");
            }
        }, 2000);
    });
}

buscaDadosDoServidor().then((mensagem)=> {
    console.log(mensagem);
}).catch((erro)=>{
console.erro(erro)
});

const minhaFuncaoAssincrona = async () =>{
    try{
const resultado = await buscaDadosDoServidor();
console.log(resultado);
    } catch(erro){
        console.erro(erro);
    }
    
}

minhaFuncaoAssincrona();

console.log("final da executando");
