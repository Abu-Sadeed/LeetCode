class Solution {
	public int longestOnes(int[] nums, int k) {
		int n = nums.length;
		if (n < 2 && k < 0)
			return n;

		int l = 0, r = 0;

		int maxlen = 0, counter = 0;
		while (r < n) {
			if (nums[r] == 0) {
				counter++;
			}
			while (k < counter) {
				if (nums[l] == 0) {
					counter--;

				}
				l++;
			}
			maxlen = Math.max(maxlen, r - l + 1);
			r++;
		}
		return maxlen;
	}
}