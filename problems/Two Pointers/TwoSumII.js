var twoSum = function (numbers, target) {
	let l = 1;
	var n = numbers.length;
	let r = n;

	while (l < r) {
		if (target == numbers[l] + numbers[r]) {
			return [l + 1, r + 1];
		} else if (target > numbers[l] + numbers[r]) {
			l++;
		} else if (target < numbers[l] + numbers[r]) {
			r--;
		}
	}
};

console.log(twoSum([2, 7, 11, 15], 9));
