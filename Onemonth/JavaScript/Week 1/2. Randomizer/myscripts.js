// Our List of Bars
document.write('<h1>Your Visit Randomizer Inside Uzbekistan</h1>')
var bars = [
    'Xiva',
    'Toshkent',
    'Buxoro',
    'Samarqand',
    'Farg`ona',
    'Namangan',
    'Andijon',
    'Jizzax',
    'Surxondaryo',
    'Qashqadaryo',
];

// Our List of Friends
var friends = [
    'Sarvar',
    'Lola',
    'Erkin',
    'Asal',
    'Ravshan',
    'Yulduz',
    'Sanjar',
    'Barno',
    'Kozim',
    'Xurshida'
];

var randomNumber = Math.floor(Math.random()*friends.length);

var barname = bars[randomNumber];
var friendname = friends[randomNumber];

    if (barname === "Xiva") {
    document.write('<img src="images/Xiva.jpg" width="800" height="400">')
     }
    else if (barname === "Toshkent") {
   document.write('<img src="images/Toshkent.jpg" width="800" height="400">')
      }
    else if (barname === "Buxoro") {
        document.write('<img src="images/Buxoro.jpg" width="800" height="400">')
    }
    else if (barname === "Samarqand") {
        document.write('<img src="images/Samarqand.jpg" width="800" height="400">')
    }
    else if (barname === "Farg`ona") {
        document.write('<img src="images/Farg`ona.jpg"" width="800" height="400">')
    }
    else if (barname === "Namangan") {
        document.write('<img src="images/Namangan.jpg" width="800" height="400">')
    }
    else if (barname === "Andijon") {
        document.write('<img src="images/Andijon.jpg" width="800" height="400">')
    }
    else if (barname === "Jizzax") {
        document.write('<img src="images/Jizzax.jpg" width="800" height="400">')
    }
    else if (barname === "Qashqadaryo") {
        document.write('<img src="images/Qashqadaryo.jpg" width="800" height="400">')
    }
    else if (barname === "Surxondaryo") {
        document.write('<img src="images/Surxondaryo.jpg" width="800" height="400">')
    }
    else {
      }

document.write("<p>You are visiting <strong>" + barname + "</strong> with <strong>" + friendname + "</strong>.</p>");
