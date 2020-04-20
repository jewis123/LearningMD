(function(exports){

	// A generic entity for our purposes. It has a basic form of physics,
	// known as verlet integration or position-based dynamics, as described
	// at http://codeflow.org/entries/2010/nov/29/verlet-collision-with-impulse-preservation

	var Entity = exports.Entity = function(x, y, width, height){
		this.pos = { x: x, y: y };
		this.ppos = { x: x, y: y };
		this.size = { x: width, y: height };
		this.halfSize = { x: width/2, y: height/2 };
		this.accel = { x: 0, y: 0 };

		this.aabb = { min: { x: 0, y: 0 }, max: { x: 0, y: 0 } };
		this._aabbArr = { min: [0, 0, 0], max: [0, 0, 0] };
		this.updateAABB(); // update immediately

		this.world = null; // reference to global world
	}

	Entity.prototype.updateAABB = function(){
		this.aabb.min.x = this.pos.x;
		this.aabb.min.y = this.pos.y;

		this.aabb.max.x = this.pos.x + this.size.x;
		this.aabb.max.y = this.pos.y + this.size.y;

		ov3.asArray( this.aabb.min, this._aabbArr.min );
		ov3.asArray( this.aabb.max, this._aabbArr.max );
	}

	// this is a bit of a misnomer, but the HSHG expects an object
	// with min/max properties pointing at arrays of coordinates
	Entity.prototype.getAABB = function(){
		return this._aabbArr;
	}

	Entity.prototype.accelerate = function(dt){
		// apply acceleration to current position, convert dt to seconds
		this.pos.x += this.accel.x * dt*dt*0.001;
		this.pos.y += this.accel.y * dt*dt*0.001;

		// reset acceleration
		this.accel.x = 0;
		this.accel.y = 0;
	}

	Entity.prototype.inertia = function(dt){

		// verlet-inate
		
		var  x = this.pos.x*2 - this.ppos.x
			,y = this.pos.y*2 - this.ppos.y;

		this.ppos.x = this.pos.x;
		this.ppos.y = this.pos.y;
		
		this.pos.x = x;
		this.pos.y = y;
	}

	Entity.prototype.draw = Entity.prototype.debugDraw = function(dt, color){
		var  ctx = this.world.screen.context
			,screen = this.world.screen;
		
		ctx.save();
		ctx.fillStyle = color || ro.colors.kpink05;
		ctx.fillRect( 
			 screen.dPos( this.pos.x ), screen.dPos( this.pos.y )
			,screen.dPos( this.size.x ), screen.dPos( this.size.y )
		);
		ctx.restore();
	}

})(ro)
