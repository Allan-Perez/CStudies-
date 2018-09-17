// call and apply 
// call(x, ...) -> calls a function with x being the value of "this" in that scope, and the rest of arguments will be the 
//					regular arguments of that function

// apply(x, [...]) -> same as call(), but the args of the funciton are set in a array.


function greet(t){
	for (let i = 0; i < t; i++) {
		console.log(`Yo what up ${this.name} ${this.lastname}`);
	}
} 
person = {
	name:"Allan",
	lastname:"Perez"
};

greet(3); // error
greet.call(person, 3) // good
greet.apply(person, [4])
