import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * @lc app=leetcode id=49 lang=java
 *
 * [49] Group Anagrams
 */

// @lc code=start
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> groupedMap = new HashMap<>();

        for (String str : strs) {
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);

            String sortedString = String.valueOf(charArr);

            groupedMap.computeIfAbsent(sortedString, k -> new ArrayList<>());

            groupedMap.get(sortedString).add(str);
        }

        return new ArrayList<>(groupedMap.values());
    }
}
// @lc code=end
