class Solution {
	public int removeDuplicates(int[] nums) {
		int n = nums.length;
		int l = 0;
		int r = 1;
		int counter = 0;

		while (r < n) {
			if (nums[l] == nums[r] && counter < 1) {
				l++;
				nums[l] = nums[r];
				counter++;
			} else if (nums[l] != nums[r]) {
				l++;
				nums[l] = nums[r];
				counter = 0;

			}
			r++;
		}
		return l + 1;
	}
}