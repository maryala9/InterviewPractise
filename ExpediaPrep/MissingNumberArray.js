function MissingNumber(arr, n) {
	if (!arr) return 'Empty Array';
	
	let x1 = arr[0];
	let x2 = 1;
	
	for (var i=2; i <= n ; i++) {
		x2 = x2 ^ i;
	}
	
	for (var i=1; i < arr.length; i++) {
		x1 = x1 ^ arr[i];
	}
	
	return x2 ^ x1;
}

console.log(MissingNumber([1,2,4,5], 5));
