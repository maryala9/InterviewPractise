function findIndexInSortedRotatedArray (array, key) {
	
	let index = indexOfRotatedArray(array, 0, array.length -1, key);
    return index;
}

function indexOfRotatedArray(arr, low, high, key) {
	if (low > high) return -1;
	
	let mid = Math.floor((low+high)/2);
	
	if (arr[mid] === key) return mid;
	
	if (arr[low] <= arr[mid]) {
		if (key <= arr[mid] && key >= arr[low]) return indexOfRotatedArray(arr, low, mid-1, key);
		return indexOfRotatedArray(arr, mid+1, high, key);
	}
	
	if (key >= arr[mid] && key <= arr[high]) return indexOfRotatedArray(arr, mid+1, high, key)
	
	return indexOfRotatedArray(arr, low , mid-1, key);
}

console.log(findIndexInSortedRotatedArray([3,4,5,1,2], 3));