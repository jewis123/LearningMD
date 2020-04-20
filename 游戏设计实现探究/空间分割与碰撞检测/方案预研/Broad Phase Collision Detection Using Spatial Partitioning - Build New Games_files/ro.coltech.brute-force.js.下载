(function(exports){

	var BruteForceTech = exports.coltech.BruteForce = function(){
		this.entities = [];
		this.collisionTests = 0;
	}

	// Brute Force does not requre an update phase
	BruteForceTech.prototype.update = ro.noop;

	BruteForceTech.prototype.addEntity = function( entity ){
		this.entities.push( entity );
	}

	BruteForceTech.prototype.removeEntity = function( entity ){
		this.entities.splice( this.entities.indexOf(entity), 1 );
	}

	BruteForceTech.prototype.queryForCollisionPairs = function(){

		var i, j, e1, e2, pairs = [], entityLen = this.entities.length;
			
		this.collisionTests = 0;

		for( i = 0; i < entityLen; i++ ){
			e1 = this.entities[i];

			for( j = i+1; j < entityLen; j++ ){
				e2 = this.entities[j];

				this.collisionTests += 1;

				if( this.aabb2DIntersection(e1, e2) === true ){
					pairs.push( [e1, e2] );
				}
			}
		}

		return pairs;
	}

	BruteForceTech.prototype.aabb2DIntersection = function( objA, objB ){
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

	BruteForceTech.prototype.draw = function(){}

})(ro);
