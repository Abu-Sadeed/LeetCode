import java.util.HashSet;

/*
 * @lc app=leetcode id=128 lang=java
 *
 * [128] Longest Consecutive Sequence
 */

// @lc code=start
class Solution {
    public int longestConsecutive(int[] nums) {
        int result = 0;
        int len = nums.length;

        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        for (int i = 0; i < len; i++) {
            int current = nums[i];
            int currentResult = 1;
            // while (set.contains(before)) {
            // set.remove(before);
            // before--;
            // }

            // while (set.contains(after)) {
            // set.remove(after);
            // after++;
            // }

            // result = Math.max(result, after - before - 1);

            if (!set.contains(current - 1)) {
                while (set.contains(current + 1)) {
                    currentResult += 1;
                    current += 1;
                }
            }
            result = Math.max(result, currentResult);
        }

        return result;
    }
}
// @lc code=end
