/*
执行用时：148 ms, 在所有 Java 提交中击败了56.53% 的用户
内存消耗：87 MB, 在所有 Java 提交中击败了93.67% 的用户
通过测试用例：24 / 24
*/

class WordsFrequency {
    HashMap<String, Integer> map = new HashMap<String, Integer>();
    public WordsFrequency(String[] book) {
        for (String s: book) {
            map.put(s, map.getOrDefault(s, 0) + 1);
        }
    }
    
    public int get(String word) {
        return map.getOrDefault(word, 0);
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * WordsFrequency obj = new WordsFrequency(book);
 * int param_1 = obj.get(word);
 */
 