// Winning a car 
let username = prompt("Hello, Who are you?"); // Functions W1 L8
    
let car = new Array("BMW", "Saab", "Maserati"); // Arrays W1 L10
    
console.log(car); // Debugging W1 11
    
    
let RandomCar = Math.floor(Math.random() * car.length);
    
let carName = car[RandomCar];
  
if(username === "Bazarov" || username==="Mehrol" ){
        
    document.write("<h1>Hello " + username + " you won a " + carName            
        + "!</h1>");  
    if (carName === "BMW") {
    document.write('<img src="images/BMW.jpg" width="1000" height="600">')
     }
    else if (carName === "Saab") {
   document.write('<img src="images/SAAB.jpg" width="1000" height="600">')
      }
  else if (carName === "Maserati") {
  document.write('<img src="images/Maserati.jpg" width="1000" height="600">')
      } 
   else {
      }
    }
    else { // conditionals W1 L9
        document.write("<h1>Hello " + username + "!");
    }