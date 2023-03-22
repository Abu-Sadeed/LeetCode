/*
 * @lc app=leetcode id=238 lang=java
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int lens = nums.length;
        int[] result = new int[lens];

        result[0] = 1;

        int r = 1;

        for (int i = 1; i < lens; i++) {
            result[i] = nums[i - 1] * result[i - 1];

        }

        for (int i = lens - 1; i >= 0; i--) {
            result[i] = result[i] * r;

            r = r * nums[i];
        }

        return result;
    }
}
// @lc code=end
