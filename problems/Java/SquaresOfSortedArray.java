class Solution {
	public int[] sortedSquares(int[] nums) {
		int n = nums.length;
		int l = 0;
		int r = n - 1;
		int[] arr = new int[n];
		int index = n - 1;

		while (l <= r) {
			int leftSqr = nums[l] * nums[l];
			int rightSqr = nums[r] * nums[r];

			if (leftSqr > rightSqr) {
				arr[index--] = leftSqr;
				l++;
			} else {
				arr[index--] = rightSqr;
				r--;
			}
		}
		return arr;
	}
}