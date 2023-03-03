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

        HashMap<Character, Integer> num_freqS = new HashMap<>();
        HashMap<Character, Integer> num_freqT = new HashMap<>();

        char[] arrayS = s.toCharArray();
        char[] arrayT = t.toCharArray();

        for (char x : arrayS) {
            num_freqS.put(x, num_freqS.getOrDefault(x, 0) + 1);
        }

        for (char x : arrayT) {
            num_freqT.put(x, num_freqT.getOrDefault(x, 0) + 1);
        }

        return num_freqS.equals(num_freqT);
    }
}
// @lc code=end
