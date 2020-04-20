(function(exports){

	///////////////////////////////////////////////////////////////////////////
	//
	// ro.js, a quick canvas-based game engine to demonstrate broad-phase
	// collision detection!
	//
	// Originally named 'fuss' for 'no fuss framework', then 'fus' to be 
	// shorter, then... 
	// [X hours of Skyrim later...] 
	// ro!
	//
	// MIT Licensed, 2012 Andrew Petersen <senofpeter@gmail.com>
	//
	///////////////////////////////////////////////////////////////////////////

	// create our namespaces
	var ro = exports.ro = exports.ro || {};
	ro.noop = function(){};
	ro.math = ro.math || {};

	ro.colors = {
		 kred05: 'rgba( 196, 101, 104, 0.5 )'
		,kpink05: 'rgba( 249, 208, 208, 0.5 )'
		,kred10: 'rgba( 196, 101, 104, 1 )'
		,kpink10: 'rgba( 249, 208, 208, 1 )'
	};

	ro.coltech = ro.coltech || {};
	// each collision tech will have the following interface:
	//		update: reread positions, update internal structure, etc
	// 		addEntity: instruct the tech to handle an entity
	// 		removeEntity: instruct the tech to stop handling an entity	
	//		queryForCollisionPairs: returns an array of arrays, with possible colliding entities

	ro.Signal = function(context){
		this.slots = [];
		this.context = context || this;
	}

	ro.Signal.prototype.add = function(f, c){
		this.slots.push({ f: f, c: c || this.context});
	}

	ro.Signal.prototype.dispatch = function(){
		var  slots = this.slots.slice(0)
		    ,len
		    ,i
		    ,ret
		    ,con;

		for (i = 0, len = slots.length; i < len; i++){
			con = slots[i];
			ret = con.f.apply(con.c, arguments);
			if(ret === false){
				break;
			}
		}
	}

	ro.Signal.prototype.remove = function(f){
		this.slots.splice(this.slots.indexOf(f), 1);
	}

	///////////////////////////////////////////////////////////////////////////
	// SHIMS

	// requestAnimationShim via: 
	// http://paulirish.com/2011/requestanimationframe-for-smart-animating/
	;(function() {
		var lastTime = 0;
		var vendors = ['ms', 'moz', 'webkit', 'o'];
		for(var x = 0; x < vendors.length && !window.requestAnimationFrame; ++x) {
			window.requestAnimationFrame = window[vendors[x]+'RequestAnimationFrame'];
			window.cancelAnimationFrame = 
			  window[vendors[x]+'CancelAnimationFrame'] || window[vendors[x]+'CancelRequestAnimationFrame'];
		}
	 
		if (!window.requestAnimationFrame)
			window.requestAnimationFrame = function(callback, element) {
				var currTime = new Date().getTime();
				var timeToCall = Math.max(0, 16 - (currTime - lastTime));
				var id = window.setTimeout(function() { callback(currTime + timeToCall); }, 
				  timeToCall);
				lastTime = currTime + timeToCall;
				return id;
			};
	 
		if (!window.cancelAnimationFrame)
			window.cancelAnimationFrame = function(id) {
				clearTimeout(id);
			};
	}());

})(window);