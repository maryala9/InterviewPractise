//combination sum
var ans, result;
function dfs(array, sum, index, target) {
	
	if (sum == target) {
		let temp = result.map(function(num) {
			return num;
		})
		
		ans.push(temp);
		
		return;
	}
	
	if (index < array.length) {
		for (var i= index; i < array.length; i++) {
			if (sum + array[i] > target) continue;
			result.push(array[i]);
			dfs(array, sum + array[i], i+1, target)
			result.pop();
		}
	}
}

function CombinationSum(array, target) {
	ans = []
	array.sort(function (a, b){
		return a-b;
	})
	if (!array) return 0;
	for (var i=0; i < array.length; i++) {
		result = [array[i]]
		dfs(array, array[i], i+1, target)
	}
	
	return ans;
}


console.log(CombinationSum([1,3,2,6,3], 6));