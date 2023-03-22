/*
 * @lc app=leetcode id=238 lang=java
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int lens = nums.length;

        int[] left = new int[lens];
        int[] right = new int[lens];
        int[] result = new int[lens];

        left[0] = 1;
        right[lens - 1] = 1;

        for (int i = 1; i < lens; i++) {
            left[i] = nums[i - 1] * left[i - 1];

        }

        for (int i = lens - 2; i >= 0; i--) {
            right[i] = nums[i + 1] * right[i + 1];
        }

        for (int i = 0; i < lens; i++) {
            result[i] = left[i] * right[i];
        }

        return result;
    }
}
// @lc code=end
