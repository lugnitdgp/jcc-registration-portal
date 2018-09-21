// select the canvas
var matrix = document.getElementById("matrix");

// make canvas fill the screen
var matrixWidth = matrix.width = window.innerWidth;
var matrixHeight =  matrix.height = window.innerHeight;

// Get canvas context
var ctx = matrix.getContext('2d');

// Returns a random integer between min (included) and max (included)
function getRandom(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// configrations 
var fontSize = 20,
	color = '#00FF98',
	background = 'rgba(2, 2, 33, 0.2)',
	speed = 125;
	charSet = "JCC 11111100010";
	charSet = charSet.split('');

// calculations 
var matrixWidth = matrixWidth,
	matrixHeight = matrixHeight,
	columns = matrixWidth/fontSize,
	rows = matrixHeight/fontSize,
	charNumber = charSet.length - 1;

// set font size
ctx.font  = fontSize + "px Arial";


draw = function() {
	setInterval(rain(), speed);
};

// the working code
// One drop per column, row set randomly
var drops = [];
for (var column = 0; column < columns; column++) {
  drops[column] = getRandom(0, rows);
}

function rain() {

	// clear the screen with opacity of 0.05
	ctx.fillStyle = background;
 	ctx.fillRect(0, 0, matrixWidth, matrixHeight);

	// For each column / drop
	for (var column = 0; column < drops.length; column++) {
		ctx.fillStyle = color;
		// pick rundwon char
		var char = charSet[getRandom(0, charSet.length - 1)];
		// Draw the char
		ctx.fillText(char, column * fontSize, drops[column] * fontSize);
		// Randomly reset drop back to top row
		if (Math.random() > 0.98) {
			drops[column] = 0;
		}

		drops[column]++; // Move drop down a row

	}
};

function run() {
	setInterval(rain, speed);
}
run();