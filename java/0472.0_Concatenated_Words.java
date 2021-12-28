/*
执行用时：1237 ms, 在所有 Java 提交中击败了19.61% 的用户
内存消耗：43.3 MB, 在所有 Java 提交中击败了93.14% 的用户
通过测试用例：44 / 44
*/

class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> ans = new ArrayList<>();
        Set<String> preWords = new HashSet<>();
        Arrays.sort(words, (s1, s2) -> (s1.length() - s2.length()));
        for (int i = 0; i < words.length; i++) {
            if (canForm(words[i], preWords)) {
                ans.add(words[i]);
            } else {
                preWords.add(words[i]);
            }
        }
        return ans;
    }

    private static boolean canForm(String word, Set<String> dict) {
        if (dict.isEmpty()) return false;
        boolean[] dp = new boolean[word.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= word.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (!dp[j]) continue;
                if (dict.contains(word.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[word.length()];
    }
}
