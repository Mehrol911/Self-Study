
var reset = document.getElementById("reset");

reset.addEventListener('click', function(){
            
var h1 = document.querySelector("h1");
h1.innerHTML = "I'm Mr. JavaScript";
console.log(h1);

})

var a = document.getElementsByClassName("howareyou");

a[0].addEventListener('click', function(){
               
var h1 = document.querySelector("h1");
h1.innerHTML = "I'm a alive!";
 console.log(h1);
 })
   
