class Solution {
	public int removeDuplicates(int[] nums) {
		int n = nums.length;
		int l = 0;
		int r = 1;

		while (r < n) {
			if (nums[l] != nums[r] && r == l + 1) {
				r++;
				l++;
			} else if (nums[l] == nums[r]) {
				r++;
			} else {
				int temp = nums[l];
				nums[l + 1] = nums[r];
				nums[r] = temp;
				r++;
				l++;
			}
		}
		return l + 1;
	}
}