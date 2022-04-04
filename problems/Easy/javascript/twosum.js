//* Initial Solve n^2 prolly

var twoSum = function (nums, target) {
	for (let i = 0; i < nums.length; i++) {
		for (let j = nums.length; j >= i + 1; j--) {
			if (nums[i] + nums[j] === target) {
				return [i, j]

			}
		}
	}

};

//* Using complements

var twoSum = function (nums, target) {
	for (let i = 0; i < nums.length; i++) {
		let val = target - nums[i];
		let j = nums.indexOf(val);

		if (j !== -1 && j !== i) {
			return [i, j]
		}
	}

};

//# JS Is slower than python 