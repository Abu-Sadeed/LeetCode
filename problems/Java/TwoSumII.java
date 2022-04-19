class Solution {
	public int[] twoSum(int[] numbers, int target) {
		int n = numbers.length;
		int l = 0;
		int r = n - 1;
		while (l < r) {
			int sum = numbers[r] + numbers[l];
			if (sum == target) {
				return new int[] { l + 1, r + 1 };
			} else if (sum < target) {
				l++;
			} else if (sum > target) {
				r--;
			}
		}
		return new int[] { -1, -1 };
	}
}
