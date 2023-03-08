import java.util.*;

/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        HashMap<Integer, Integer> valueMap = new HashMap<>();

        for (int i = 0; i < len; i++) {
            int reminder = target - nums[i];

            if (valueMap.get(reminder) != null) {
                return new int[] { valueMap.get(reminder), i };

            } else {
                valueMap.put(nums[i], i);
            }

        }

        return new int[] {};
    }
}
// @lc code=end
