(function(exports){

	var SpatialGridTech = exports.coltech.SpatialGrid = function( minX, minY, maxX, maxY, cellSize ){
		this.entities = [];

		this.min = ov3( minX, minY );
		this.max = ov3( maxX, maxY );
		this.pxCellSize = cellSize;
		this.grid = [[]];

		// these are purely for reporting purposes
		this.collisionTests = 0;
		this.totalCells = 0;
		this.allocatedCells = 0;
		this.hashChecks = 0;
	}

	SpatialGridTech.prototype.update = function(){
	
		var  cGridWidth = Math.floor( (this.max.x - this.min.x) / this.pxCellSize )
			,cGridHeight = Math.floor( (this.max.y - this.min.y) / this.pxCellSize )
			,cXEntityMin
			,cXEntityMax
			,cYEntityMin
			,cXEntityMax
			,i
			,j
			,entity
			,cX
			,cY
			,gridCol
			,gridCell;

		// the total number of cells this grid will contain
		this.totalCells = cGridWidth * cGridHeight;
		this.allocatedCells = 0;

		// construct grid
		// NOTE: this is a purposeful use of the Array() constructor 
		this.grid = Array(cGridWidth);
		
		// insert all entities into grid
		for( i = 0; i < this.entities.length; i++ ){
			entity = this.entities[i];

			// if entity is outside the grid extents, then ignore it
			if( 
				entity.pos.x < this.min.x || entity.pos.x > this.max.x
				|| entity.pos.y < this.min.y || entity.pos.y > this.max.y 
			){
				continue;
			}

			// find extremes of cells that entity overlaps
			// subtract min to shift grid to avoid negative numbers
			cXEntityMin = Math.floor( (entity.pos.x - this.min.x) / this.pxCellSize );
			cXEntityMax = Math.floor( (entity.pos.x + entity.size.x - this.min.x) / this.pxCellSize );
			cYEntityMin = Math.floor( (entity.pos.y - this.min.y) / this.pxCellSize );
			cYEntityMax = Math.floor( (entity.pos.y + entity.size.y - this.min.y) / this.pxCellSize );

			// insert entity into each cell it overlaps
			// we're looping to make sure that all cells between extremes are found
			for( cX = cXEntityMin; cX <= cXEntityMax; cX++ ){

				// make sure a column exists, initialize if not to grid height length
				// NOTE: again, a purposeful use of the Array constructor 
				if ( !this.grid[cX] ){ this.grid[cX] = Array( cGridHeight ); }

				gridCol = this.grid[cX];

				// loop through each cell in this column
				for( cY = cYEntityMin; cY <= cYEntityMax; cY++ ){

					// ensure we have a bucket to put entities into for this cell
					if ( !gridCol[cY] ){ 
						gridCol[cY] = [];

						// this is for stats purposes only
						this.allocatedCells	+= 1;
					}

					gridCell = gridCol[cY];

					// add entity to cell
					gridCell.push( entity );
				}
			}
		}

	}
	
	SpatialGridTech.prototype.addEntity = function( entity ){
		this.entities.push( entity );
	}
	
	SpatialGridTech.prototype.removeEntity = function( entity ){
		this.entities.splice( this.entities.indexOf(entity), 1 );
	}

	SpatialGridTech.prototype.queryForCollisionPairs = function(){

		var checked = {}
			,pairs = []
			,entityA
			,entityB
			,hashA
			,hashB
			,i
			,j
			,k
			,l
			,gridCol
			,gridCell

		// reset counts, for debug/comparison purposes
		this.collisionTests = 0;
		this.hashChecks = 0;

		// for every column in the grid...
		for( i = 0; i < this.grid.length; i++ ){

			gridCol = this.grid[i];

			// ignore columns that have no cells
			if( !gridCol ){ continue; }

			// for every cell within a column of the grid...
			for( j = 0; j < gridCol.length; j++ ){

				gridCell = gridCol[j];

				// ignore cells that have no objects
				if( !gridCell ){ continue; }

				// for every object in a cell...
				for( k = 0; k < gridCell.length; k++ ){

					entityA = gridCell[k];

					// for every other object in a cell...
					for( l = k+1; l < gridCell.length; l++ ){

						entityB = gridCell[l];

						// create a unique key to mark this pair.
						// use both combinations to ensure linear time
						hashA = entityA._roId + ':' + entityB._roId;
						hashB = entityB._roId + ':' + entityA._roId;

						this.hashChecks += 2;

						if( !checked[hashA] && !checked[hashB] ){
							
							// mark this pair has checked
							checked[hashA] = checked[hashB] = true;

							this.collisionTests += 1;

							if( this.aabb2DIntersection( entityA, entityB ) ){
								pairs.push( [entityA, entityB] );
							}
						}
					}
				}
			}
		}

		return pairs;
	}		

	// this is taken verbatim from the BruteForceTech
	SpatialGridTech.prototype.aabb2DIntersection = function( objA, objB ){
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

	SpatialGridTech.prototype.draw = function( ctx ){
		
		var  i
			,j
			,x
			,y
			,cGridWidth = Math.floor( (this.max.x - this.min.x) / this.pxCellSize )
			,cGridHeight = Math.floor( (this.max.y - this.min.y) / this.pxCellSize );

		ctx.save();
		ctx.strokeStyle = 'rgba( 0, 0, 0, 0.1 )';

		for( i = 0; i < cGridWidth; i++ ){

			x = this.min.x + ( i * this.pxCellSize );
			
			ctx.beginPath();
			ctx.moveTo( x, 0 );
			ctx.lineTo( x, this.max.y );
			ctx.stroke();

		}

		for( j = 0; j < cGridHeight; j++ ){

			y = this.min.y + ( j * this.pxCellSize );

			ctx.beginPath();
			ctx.moveTo( 0, y );
			ctx.lineTo( this.max.x, y );
			ctx.stroke();
		}

		ctx.restore();

		ctx.fillText( 
			'Total Cells: ' + this.totalCells
			,10, 50 
		);

		ctx.fillText( 
			'Allocated Cells: ' + this.allocatedCells
			,10, 68 
		);

		ctx.fillText( 
			'Hash Checks: ' + this.hashChecks
			,10, 86 
		);
	}
})(ro);
