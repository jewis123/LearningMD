(function(exports){

	var Screen = exports.Screen = function(canvas, scale){

		scale = scale || 1;

		this.context = canvas.getContext('2d');
		this.canvas = canvas;

		this.scale = scale;
		this.size = { x: canvas.width, y: canvas.height };
		this.realSize = { x: canvas.width * scale, y: canvas.height * scale };

	}

	Screen.prototype.dPos = function(i){
		return Math.round(i * this.scale);
	}

})(ro);