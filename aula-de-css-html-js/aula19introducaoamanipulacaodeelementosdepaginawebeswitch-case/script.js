// function trocaCor()
//     {
// const div1 = document.getElementById("div-1");  
// const div2 = document.getElementById("div-2"); 
//  const div3 = document.getElementById("div-3");

//  div.style.backgroundColor = "red";
//   div.style.backgroundColor = "pink";
//    div.style.backgroundColor = "blue";
//     }

//     function trocaCor()
//     {
//    const div1 = document.getElementById("div-1");  
// const div2 = document.getElementById("div-2"); 
//  const div3 = document.getElementById("div-3");     
//     }

    
//  div.style.backgroundColor = "";
//   div.style.backgroundColor = "";
//    div.style.backgroundColor = "";

function efetuaOperacao()
{
    let num1 = parseFloat(  document.getElementById("num1").value);
    let num2 = parseFloat ( document.getElementById("num2").value);
    let operador = parseFloat (document.getElementById("operador").value);


switch (operador){

case "+":
    resultado = num1 + num2;
    break;

case "-":
    resultado = num1 - num2;
    break;

    case "*":
    resultado = num1 * num2;
    break;

    case "/":
    resultado = num1 / num2;
    break;
    default:

}

document.getElementById("resultado").innerHTML

}