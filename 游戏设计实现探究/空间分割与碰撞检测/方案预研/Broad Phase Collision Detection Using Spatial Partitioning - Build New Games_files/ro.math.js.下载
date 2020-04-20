(function(exports){

	// return value rounded to the nearest multiple of multiple
	exports.math.toNearest = function( value, multiple ){
		var rem = value % multiple
			,result = value - rem;

		if( rem > multiple/2 ){
			result += multiple;
		}

		return result;
	}

	// Compute the nearest point along a normal that is a multiple of 16 (for example),
	// for tile math purposes.
	exports.math.toNearestAlong = function( point, normal, multiple ){

		var  nearestX = ro.math.toNearest( point.x, multiple )
			,nearestY = ro.math.toNearest( point.y, multiple )

			,vertRes = {} 
			,horiRes = {} 

		ro.math.intersectLineLine( 
			point.x, point.y, point.x + normal.x, point.y + normal.y,
			nearestX, point.y, nearestX, point.y + 1, vertRes);
		ro.math.intersectLineLine( 
			point.x, point.y, point.x + normal.x, point.y + normal.y,
			point.x, nearestY, point.x + 1, nearestY, horiRes);

		var  vertDist = ov3.distance( point, vertRes.line )
			,horiDist = ov3.distance( point, horiRes.line )

		if( !vertRes.line && horiRes.line ){
			return horiRes.line;
		} 

		if( vertRes.line && !horiRes.line ){
			return vertRes.line;
		} 

		return vertDist < horiDist
			? vertRes.line
			: horiRes.line;
	}

	exports.math.angleTo = function( v1x, v1y, v2x, v2y ){

		var v1atan = Math.atan2( v1y, v1x )
			,v2atan = 0;

		if( v2x != null && v2y != null ){
			v2atan = Math.atan2( v2y, v2x );
			return v2atan - v1atan;
		}

		return v1atan;
	}

	// adapted/ported from: http://paulbourke.net/geometry/lineline2d/Helpers.cs
	exports.math.intersectLineLine = function(a1x, a1y, a2x, a2y, b1x, b1y, b2x, b2y, res){

		res = res || {};
		res.parallel = false;
		res.coincidental = false;
		res.line = false;
		res.segment = false;

		var denom = (b2y - b1y) * (a2x - a1x) - (b2x - b1x) * (a2y - a1y)
			,n_a = (b2x - b1x) * (a1y - b1y) - (b2y - b1y) * (a1x - b1x)
			,n_b = (a2x - a1x) * (a1y - b1y) - (a2y - a1y) * (a1x - b1x);

		// check for lines being parallel (or possibly coincidental)
		if( denom == 0 ){
			res.parallel = true;

			if( n_a === 0 && n_b === 0 ){
				res.coincidental = true;
			}

			return false
		}

		// calculate the scalar (fractional) that determines where each line 
		// could intersect (t in many versions)
		var  ua = n_a / denom
			,ub = n_b / denom;

		res.line = { 
			 x: a1x + ( ua * (a2x - a1x) )
			,y: a1y + ( ua * (a2y - a1y) )
		};

		// test if segments intersect. 0 >= ua <= 1 implies intersection of 
		// the given segments, while 0 > ua > 1 implies that only the defined 
		// lines intersect
		if( ua >= 0 && ua <= 1 && ub >= 0 && ub <= 1 ){
			res.segment = res.line;	
		}

		return true;
	}


	// vector utility, for working with plain objects having x, y, and/or z properties

	var ov3 = window.ov3 = exports.ov3 = function(x, y, z){
		return {
			x: x || 0,
			y: y || 0,
			z: z || 0
		}
	};

	ov3.asArray = function( v1, target ){

		if( !target ){
			target = [ v1.x, v1.y, v1.z || 0 ]
		} else {
			target[0] = v1.x;
			target[1] = v1.y;
			target[2] = v1.z || 0;
		}

		return target;
	}

	ov3.fromArray = function( v1arr, target ){
		target = target || ov3();

		target.x = v1arr[0];
		target.y = v1arr[1];
		target.z = v1arr[2] || 0;

		return target;
	}

	ov3.add = function(v1, v2, target){

		if( typeof target !== 'object' ) target = v1;

		target.x = v1.x + v2.x;
		target.y = v1.y + v2.y;
		target.z = (v1.z || 0) + (v2.z || 0);

		return target;
	}

	ov3.sub = function(v1, v2, target){

		if( typeof target !== 'object' ) target = v1;

		target.x = v1.x - v2.x;
		target.y = v1.y - v2.y;
		target.z = (v1.z || 0) - (v2.z || 0);

		return target;
	}

	ov3.mult = function(v1, v2, target){

		if( typeof target !== 'object' ) target = v1;

		target.x = v1.x * v2.x;
		target.y = v1.y * v2.y;
		target.z = (v1.z || 0) * (v2.z || 0);

		return target;
	}

	ov3.scale = function(v1, x, target){
		if(!target) target = v1;

		target.x = v1.x * x;
		target.y = v1.y * x;
		target.z = v1.z * x || 0;

		return target;
	}

	ov3.normalize = function(v1, target){
		if(!target) target = v1;

		var  x = v1.x
			,y = v1.y
			,z = v1.z || 0
			,sqrt = Math.sqrt(x*x + y*y + z*z)

		if( sqrt == 0 ){
			target.x = target.y = target.z = 0;
			return target;
		}

		var len = 1 / sqrt;

		target.x = x * len;
		target.y = y * len;
		target.z = z * len;

		return target;
	}

	ov3.length = function(v1){

		var  x = v1.x
			,y = v1.y
			,z = v1.z || 0

		return Math.sqrt(x*x + y*y + z*z);
	}

	ov3.distance = function(v1, v2){

		var  x = v1.x - v2.x
			,y = v1.y - v2.y
			,z = (v1.z || 0) - (v2.z || 0)

		return Math.sqrt(x*x + y*y + z*z);
	}

	ov3.dot = function( v1, v2 ){
		return v1.x*v2.x + v1.y*v2.y + (v1.z || 0)*(v2.z || 0);
	}

	ov3.direction = function( v1, v2, target ){

		target = target || v1;

		var  x = v2.x - v1.x
			,y = v2.y - v1.y
			,z = v2.z - v1.z || 0
			,len = Math.sqrt(x*x + y*y + z*z);

		if (!len) { 
			target.x = 0; 
			target.y = 0; 
			target.z = 0;
			return target; 
		}
		
		len = 1 / len;
		target.x = x * len; 
		target.y = y * len; 
		target.z = z * len;

		return target;
	}

	ov3.negate = function( v1, target ){

		target = target || v1;

		target.x = v1.x * -1;
		target.y = v1.y * -1;
		target.z = (v1.z * -1) || 0;

		return target;
	}

	// rotate v1 around the origin given an angle
	// angle can also be a normalized vector to save on cos/sin calcs
	ov3.rotateZ = function( v1, angle, target ){

		target = target || v1;

		var  cosa = angle.x !== undefined
				? angle.x
				: Math.cos(angle)
			,sina = angle.y !== undefined
				? angle.y
				: Math.sin(angle)
			,x = v1.x
			,y = v1.y

		target.x = cosa * x - sina * y;
		target.y = sina * x + cosa * y;
		target.z = v1.z || 0;

		return target;	
	}

	ov3.angleTo = function( v1, v2 ){

		var v1atan = Math.atan2( v1.y, v1.x )
			,v2atan = 0;

		if( v2 ){
			v2atan = Math.atan2( v2.y, v2.x )
			return v2atan - v1atan;
		}

		return v1atan;
	}

	ov3.intersect = function( a, b, c, d, res ){
		return ro.math.intersectLineLine(a.x, a.y, b.x, b.y, c.x, c.y, d.x, d.y, res);
	}

	ov3.str = function( v1 ){
		return '{ x: ' + v1.x + ', y: ' + v1.y + ', z: ' + v1.z + ' }';
	}

})(ro)