function SpiralMatrix(matrix) {
	let result = [];
	if (!matrix || matrix.length === 0 || matrix[0].length === 0) {
		return result; 
	}

	let rows = matrix.length;
	let cols = matrix[0].length;
	
	let x = 0, y = 0;
	
	while (rows > 0 && cols > 0) {
		if (rows == 1) {
			for (var i=0; i < cols; i++) {
				result.push(matrix[x][y++]);
			}
			break;
		} else if (cols == 1) {
			for (var i=0; i< rows; i++) {
				result.push(matrix[x++][y]);
			}
			break;
		}
		for (var i =0; i < cols-1; i++) {
			result.push(matrix[x][y++]);
		}
		for (var i =0; i < rows-1; i++) {
			result.push(matrix[x++][y]);
		}
		for (var i =0; i < cols-1; i++) {
			result.push(matrix[x][y--]);
		}
		for (var i =0; i < rows-1; i++) {
			result.push(matrix[x--][y]);
		}
		
		rows -= 2;
		cols -=2;
		
		x++;
		y++;
	}
	
	return result;

}

console.log(SpiralMatrix([[1,2,3],[4,5,6],[7,8,9]]));


// I am always an exciting person when i work with large data and bigger applications as i know there would be a lot to tackle and pretty hard problems. For me to host my website as an amazon s3 static webpage and a simple Lambda function later moved it to github static page io page. I am really interested in this job is that i am excited to work on Full stack technologies and grow my career. Also taking ownership of what i do is something that always helped me to grow big which redems with amazon principles