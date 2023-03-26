import java.util.Stack;

/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        Stack<Character> bracketPair = new Stack();

        for (Character c : s.toCharArray()) {
            switch (c) {
                case '(':
                case '{':
                case '[':
                    bracketPair.push(c);
                    break;
                case ')':
                    if (bracketPair.isEmpty() || bracketPair.pop() != '(') {
                        return false;
                    }
                    break;
                case '}':
                    if (bracketPair.isEmpty() || bracketPair.pop() != '{') {
                        return false;
                    }
                    break;
                case ']':
                    if (bracketPair.isEmpty() || bracketPair.pop() != '[') {
                        return false;
                    }
            }

        }
        return bracketPair.isEmpty();
    }
}
// @lc code=end
