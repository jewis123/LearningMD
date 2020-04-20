(function(exports){

	var Input = exports.Input = function( element ){
		this.down = {};
		this.activeStates = {};
		this.bindingsKeyToState = {};

		element = element || document;

		element.addEventListener('keyup', this._onKeyUp.bind(this), false);
		element.addEventListener('keydown', this._onKeyDown.bind(this), false);
	}

	Input.prototype.bind = function(keyCode, name){
		if( !this.bindingsKeyToState[keyCode] ){
			this.bindingsKeyToState[keyCode] = [];
		}

		this.bindingsKeyToState[keyCode].push( name );
	}

	Input.prototype.pressed = function(name){
		return this.activeStates[name]
			? true
			: false;
	}

	Input.prototype._onKeyUp = function(e){

		delete this.down[e.which];

		var states = this.bindingsKeyToState[e.which]
			,i;

		if( states ){
			e.stopPropagation();
			e.preventDefault();

			for( i = 0; i < states.length; i++ ){
				delete this.activeStates[ states[i] ];
			}

			return false;
		}
	}

	Input.prototype._onKeyDown = function(e){

		this.down[e.which] = true;

		var states = this.bindingsKeyToState[e.which]
			,i;

		if( states ){
			e.stopPropagation();
			e.preventDefault();

			for( i = 0; i < states.length; i++ ){
				this.activeStates[ states[i] ] = true;
			}

			return false;
		}
	}

})(ro);