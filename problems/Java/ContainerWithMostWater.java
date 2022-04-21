class Solution {
	public int maxArea(int[] height) {
		int n = height.length;
		int l = 0;
		int r = n - 1;
		int capacity = 0;
		int currentCap = 0;

		while (l < r) {
			int width = r - l;
			if (height[l] > height[r]) {
				currentCap = height[r] * width;
				r--;
			} else {
				currentCap = height[l] * width;
				l++;
			}

			capacity = Math.max(currentCap, capacity);

		}
		return capacity;
	}
}