 //Functions that remmember which scope do they belong to, and 
 // can move to that same scope whenever they are called, recovering 
 // every variable in that scope.

 //What this is about basically is that a function that is returned from another function
 // can remember the scope of the "father" function:


 function greetFamily(lastName){
 	return function greetName(name){
 		console.log(`What up ${name} ${lastName}`);
 	}
 }


 const greetGomez = greetFamily("Gomez");
 const greetPerez = greetFamily("Perez");


 greetGomez("Fernando");
 greetPerez("Alfred");