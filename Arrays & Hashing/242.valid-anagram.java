import java.util.HashMap;

/*
 * @lc app=leetcode id=242 lang=java
 *
 * [242] Valid Anagram
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        int firstLen = s.length();
        int secondLen = t.length();
        if (firstLen != secondLen) {
            return false;
        }

        HashMap<Character, Integer> numFreqS = new HashMap<>();
        HashMap<Character, Integer> numFreqT = new HashMap<>();

        char[] arrayS = s.toCharArray();
        char[] arrayT = t.toCharArray();

        for (char x : arrayS) {
            numFreqS.put(x, numFreqS.getOrDefault(x, 0) + 1);
        }

        for (char x : arrayT) {
            numFreqT.put(x, numFreqT.getOrDefault(x, 0) + 1);
        }

        return numFreqS.equals(numFreqT);
    }
}
// @lc code=end
