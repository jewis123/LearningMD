(function(exports){

	var World = exports.World = function(canvasId, proto){
		this.mainHandle = null;
		this.broadPhase = proto.coltech || (new ro.coltech.BruteForce);

		this.entities = [];
		this.uniq = 0;
		this.isRunning = false;
		this.dt = 0; // delta time
		this.pdt = 0; // previous delta time
		this.pts = 0; // previous timestamp from rAF

		// very simple custom extend
		var p;
		for(p in proto){
			if( proto.hasOwnProperty( p ) ){
				this[p] = proto[p];
			}
		}

		this.scale = proto.scale || 1;
		this.screen = new ro.Screen( document.getElementById(canvasId), this.scale );

		this.input = new ro.Input();

		if(this.debug === true){
			var stats = this.stats = new Stats();
			stats.setMode(0); // 0: fps, 1: ms

			// Align top-right
			stats.domElement.style.position = 'absolute';
			stats.domElement.style.right = '0px';
			stats.domElement.style.top = '0px';

			document.body.appendChild( stats.domElement );
		}

		if( this.init ){
			this.init();
		}
	}

	// expected that the user will handle these
	World.prototype.update = ro.noop;
	World.prototype.handleCollisions = ro.noop;

	World.prototype.draw = function(dt){

		var i, entity, ctx = this.screen.context;
		for(i = 0; i < this.entities.length; i++){
			entity = this.entities[i];
			entity.draw();
		}

	}	

	World.prototype.step = function(dt){

		if(this.debug === true){
			this.stats.begin();
		}

		var i, entity, screen = this.screen, ctx = this.screen.context;

		screen.context.clearRect( 0, 0, screen.realSize.x, screen.realSize.y );

		this.draw(dt);

		for(i = 0; i < this.entities.length; i++){
			entity = this.entities[ i ];
			entity.accelerate(dt);
			entity.updateAABB();
		}

		// do collision stuff
		this.broadPhase.update();
		var collisions = this.broadPhase.queryForCollisionPairs();
		this.handleCollisions( dt, collisions );

		for(i = 0; i < this.entities.length; i++){
			entity = this.entities[ i ];
			entity.inertia(dt);
			entity.updateAABB();
		}		

		this.update(dt);

		if(this.debug === true){
			this.stats.end();

			ctx.font = '12pt Arial';

			ctx.fillText( 
				'Collision Tests: ' + this.broadPhase.collisionTests
				,10, 14
			);

			ctx.fillText( 
				'Entities: ' + this.entities.length
				,10, 32
			);

			this.broadPhase.draw(ctx)
		}
	}

	World.prototype.start = function(){

		var self = this;
		
		this.isRunning = true;

		var func = function(dt){
			self.mainHandle = window.requestAnimationFrame( func );
			self.pdt = self.dt;
			self.dt = dt - self.pts;
			self.pts = dt;
			self.step(self.dt);
		};
		
		func(Date.now());
	}

	World.prototype.stop = function(){
		this.isRunning = false;
		window.cancelAnimationFrame( this.mainHandle );
	}

	World.prototype.addEntity = function(entity){
		entity._roId = this.uniq++;
		entity.world = this;
		this.entities.push( entity );
		this.broadPhase.addEntity( entity );
	}

	World.prototype.removeEntity = function(entity){
		delete entity._roId;
		delete entity.world;
		this.entities.splice( this.entities.indexOf(entity), 1 );
		this.broadPhase.removeEntity( entity );
	}

})(ro)
