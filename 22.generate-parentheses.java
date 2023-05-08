import java.util.List;

/*
 * @lc app=leetcode id=22 lang=java
 *
 * [22] Generate Parentheses
 */

// @lc code=start
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        int count_open = 0;
        int count_close = 0;

        public void backtrack(count_open, count_close) {
            if(count_open == count_close && count_close ==n) {

            }

            if(count_open < n){
                backtrack(count_open+1, count_close);
            }
        }
    }

}
// @lc code=end
