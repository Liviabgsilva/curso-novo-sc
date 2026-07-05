function validateForm()
{

const name = document.getElementById("name").value;
const email = document.getElementById("email").value;
const message = document.getElementById("message").value;

if(name === '' || email === ''  || message === '');

{
    alert('Todos os campos sao obrigatorios');
    return false;
}

if (name.length < 3 || name.length > 50) {
    alert('O nome deve ter entre 3 e 50 caracteres');
    return false;
}


if (email.length < 5 || name.length > 50) {
    alert('O email deve ter entre 5 e 50 caracteres');
    return false;
}

const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

if (!emailPattern.test(email))
     {
 alert('Por favor insira um valor de email valido');
    return false;
}

return true;

}


document.getAnimations('contactForm').addEventListener('submit', function(event){
    event.preventDefalt();
   if( validateForm());
    {
alert("formulario validado!");
   }
});