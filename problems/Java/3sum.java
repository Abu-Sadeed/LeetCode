class Solution {
	public List<List<Integer>> threeSum(int[] nums) {
		int n = nums.length;
		List<List<Integer>> result = new ArrayList<>();
		Arrays.sort(nums);

		for (int i = 0; i < n; i++) {

			if (i != 0 && nums[i] == nums[i - 1]) {
				continue;
			}

			int l = i + 1;
			int r = n - 1;

			while (l < r) {
				int sum = nums[i] + nums[r] + nums[l];

				if (sum == 0) {
					result.add(Arrays.asList(nums[i], nums[r], nums[l]));

					l++;
					r--;

					while (l < r && nums[l] == nums[l - 1]) {
						l++;
					}
					while (l < r && nums[r] == nums[r + 1]) {
						r--;
					}

				} else if (sum > 0) {
					r--;
				} else if (sum < 0) {
					l++;
				}
			}
		}
		return result;
	}
}