const { once } require("events");

const celulas = document.querySelectorAll('.celula');


let vezDox = true;

document.getElementById("botaoReiniciar").addEventListener('click',iniciarJogo);

function iniciarJogo(){
    celulas.forEach(celula =>{
        celula.textContent = "";
        celula.addEventListener('click',tratarClique, {once:true} );

    });
}

function tratarClique(evento){
    evento.target.textContent = vezDox ? "x" : "o";
    vezDox = !vezDox;
}

iniciarJogo();