(function(exports){

	var HSHGTech = exports.coltech.HierarchicalSpatialHashGrid = function(){
		this.hshg = new HSHG();

		// these are just shortcuts
		this.addEntity = this.hshg.addObject.bind(this.hshg);
		this.removeEntity = this.hshg.removeObject.bind(this.hshg);
	}

	HSHGTech.prototype.update = function(world){
		this.hshg.update();
	}

	HSHGTech.prototype.queryForCollisionPairs = function(){
		this.collisionTests = 0;
		return this.hshg.queryForCollisionPairs(this.aabb2DIntersection.bind(this));
	}

	// this is taken verbatim from the BruteForceTech
	HSHGTech.prototype.aabb2DIntersection = function( objA, objB ){
		this.collisionTests += 1;

		var  a = objA.getAABB()
			,b = objB.getAABB();

		if(
			a.min[0] > b.max[0] || a.min[1] > b.max[1]
			|| a.max[0] < b.min[0] || a.max[1] < b.min[1]
		){
			return false;
		} else {
			return true;
		}
	}

	HSHGTech.prototype.draw = function(ctx){}

	/*
	HSHGTech.prototype.addEntity = function( entity ){
		this.hshg.addObject( entity );
	}
	
	HSHGTech.prototype.removeEntity = function( entity ){
		this.hshg.removeObject( entity );
	}
	*/

})(ro);
