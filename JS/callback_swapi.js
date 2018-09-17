//Here we practice the "callbacks" with a request to an api.
let url = "https://swapi.co/api/people/10";

function GET_(URL, CB){
	const xhr = new XMLHttpRequest();

	xhr.onreadystatechange = function(){
		const DONE = 4;
		const OK = 200;

		if(this.readyState === DONE){
			if(this.status === OK){
				CB(null, JSON.parse(this.responseText));
			} else{
				CB(new Error(`The status of the response is: ${this.status}`));
			}
		}
	}
	xhr.open('GET', URL);
	xhr.send(null);
}

function _handleErr(err){
	console.log(`Failed request: ${err}`);
}


GET_(url, function(err, resp){
	if (err) return _handleErr(err);

	GET_(resp.homeworld, function(err, resp2){
		console.log(`${resp.name} was born in ${resp2.name}`);
	})
});
//We could be chaining callback by callback by callback and lo and behold. This is called CALLBACK HELL
//We can sole it by using "promises", which are objects of the ECMAScript 2015
//and it can have 3 different states: pending, fulfilled, and rejected.
const prom = new Promise(function(resolve, reject){
	setTimeout(resolve, 1000);
});


//Now we can do the GET request of the above in a different way:
function _GET(URL){
	return new Promise(function(resl, rej){
		const xhr = new XMLHttpRequest();

	xhr.onreadystatechange = function(){
		const DONE = 4;
		const OK = 200;

		if(this.readyState === DONE){
			if(this.status === OK){
				resl(JSON.parse(this.responseText));
			} else{
				rej(new Error(`The status of the response is: ${this.status}`));
			}
		}
	}
	xhr.open('GET', URL);
	xhr.send(null);
	});
}

//Naturally, the call of the function also changes:
let mresp ;
_GET(URL).then((res) => {
			mresp = res;
			return _GET(mresp.homeworld);
		 })
		 .then((res) => {
		 	mresp.homeworld = res.name; 
		 	console.log(`${mresp.name} was born in ${mresp.homeworld}`);
		 })
		 .catch((err) => _handleErr(err));

//But we can also use fetch, which is built-in :
let mr; 
fetch(URL)
	.then(res => res.json())
	.then((res) => {
			mr = res;
			return fetch(mr.homeworld);
		 })
	.then(res => res.json())
	.then((res) => {
			mr.homeworld = res.name;
			console.log(`${mr.name} was born in ${mr.homeworld}`);
		 })
	.catch((err) => _handleErr(err));
