// There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters. 

// If possible write the function that can take an array as input to generalize the number of steps that can be climbed EX: steps = [1,2,5] Implement: fun StaireCase(N, steps)


function StairCase(n, arr) {
	var cache = [1];
	for (let i=1; i< n+1; i++) {
		let ans = getSumOfPossiblities(i, arr, cache);
		cache[i] = ans;
	}
	
	return cache[n];
}
function getSumOfPossiblities(i, arr, cache) {
	let sum = 0;
	arr.forEach(function (x) {
		if (i-x >= 0) {
			sum += cache[i-x];
		}
	});
	return sum;
}

console.log(StairCase(3,[1,3]));