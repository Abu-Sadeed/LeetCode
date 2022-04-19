class Solution {
	public void moveZeroes(int[] nums) {
		int n = nums.length;
		int l = 0;
		int r = 1;

		while (r < n) {
			if (nums[l] == 0 && nums[r] != 0) {
				int temp = nums[l];
				nums[l] = nums[r];
				nums[r] = temp;
			} else if (nums[l] != 0) {
				l++;
				r++;
			} else {
				r++;
			}
		}
	}
}