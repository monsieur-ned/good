const number = document.querySelectorAll('.number-inc');
const speed = 100;

number.forEach(element => {
	incNumber(element)
});

function incNumber(elem) {
	let text = +elem.innerText;
	const value = +elem.getAttribute("data-target")
	const inc = Math.floor(value/speed) + 1;

	if(text < value){
		elem.innerText = inc + text;

		setTimeout(() => {
			incNumber(elem)
		}, 20)
	}else{
		elem.innerText = value;
	}

}