

class Tog{
	constructor(el){
		this.el = el;
		this.el.innerHTML = 'OFF';
		this.state = 0;

		this.dictionary = [
		'OFF',
		'ON',
		'ALIEN',
		'UFO',
		'MODEL',
		'ENGINEER',
		'SEMENTAL',
		'BOTTLE',
		'IPAD',
		'SMARTPHONE'
		]

		this.el.addEventListener('click', this.onClick.bind(this));
	}

	onClick(){
		this.generateRandomState();
		this.toggleText();
	}

	toggleText(){
		this.el.innerHTML = this.dictionary[this.state];
	}

	generateRandomState(){
		this.state = Math.floor((Math.random() * 10));
	}
}

const button = document.getElementById('button');

const but = new Tog(button);