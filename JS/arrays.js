// we can pass an undefined number of params to a function 
// using SPREAD OPERATOR (..n)


//This is the easy but not correct way
function add(...n){
	let sum = 0;
	for(let i = 0; i<n.length; i++) {
		sum +=n[i];
	}
	return sum;
}


//This is the correct way
function _add(...n) {
	return n.reduce(function (a,n_){
		a+=n;
		return a;
	});
}

//This is the correct way but compressed
let add_ =  (...n) => n.reduce((a,n) => a+=n);



//*****************************************************************//
function double_incorrect(...n){
	const res = []
	for(let i=0; i<n.length; i++){
		res.push(n[i]);
	}
	return res;
}



function double_correct(...n){
	n.map(function(n_){return n_*2;})
}


let double_compressed = (...n) => n.map((n_) => n_*2);

//*****************************************************************//

function even_incorrect(...n) {
	const res = []
	for(let i=0; i<n.length; i++){
		if(n[i] % 2 == 0){
			res.push(n[i]);
		}
	}
	return res;
}


function even_correct_q(...n){
	return n.filter(function (e) {
		if(e % 2 == 0){
			return e;
		}
	})
}


function even_correct(...n){
	return n.filter(function (e) {
			return e % 2 == 0;
	})
}

let compressed = (...n) => n.filter((e) => e%2==0);