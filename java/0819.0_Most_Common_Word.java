/*
执行用时：275 ms, 在所有 Java 提交中击败了5.79% 的用户
内存消耗：41.7 MB, 在所有 Java 提交中击败了5.79% 的用户
通过测试用例：47 / 47
*/
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String [] ss = paragraph.replaceAll("[^^a-zA-Z]{1,}", " ").toLowerCase().split(" ");
        Map<String, Integer> m = new HashMap<>();
        for (String b: banned)
            m.put(b, -10000);
        String ans = "";
        int max = 0;
        for (String s: ss) {
            int i = m.getOrDefault(s, 0) + 1;
            if (i > max) {
                ans = s;
                max = i;
            }
            m.put(s, i);
        }
        return ans;
    }
}
