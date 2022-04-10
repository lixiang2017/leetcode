/*
执行用时：2 ms, 在所有 Java 提交中击败了75.06% 的用户
内存消耗：39.4 MB, 在所有 Java 提交中击败了34.41% 的用户
通过测试用例：82 / 82
*/
class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] morse = new String[]{".-","-...","-.-.","-..",".","..-.","--.","....","..",
                                        ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                                        "...","-","..-","...-",".--","-..-","-.--","--.."};
        Set<String> trans = new HashSet<>();
        for (String w: words) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < w.length(); i++) {
                sb.append(morse[w.charAt(i) - 'a']);
            }
            trans.add(sb.toString());
        }
        return trans.size();
    }
}


/*
执行用时：2 ms, 在所有 Java 提交中击败了75.06% 的用户
内存消耗：39 MB, 在所有 Java 提交中击败了72.32% 的用户
通过测试用例：82 / 82
*/
class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] morse = new String[]{".-","-...","-.-.","-..",".","..-.","--.","....","..",
                                        ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                                        "...","-","..-","...-",".--","-..-","-.--","--.."};
        Set<String> trans = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        for (String w: words) {
            sb.setLength(0);
            for (int i = 0; i < w.length(); i++) {
                sb.append(morse[w.charAt(i) - 'a']);
            }
            trans.add(sb.toString());
        }
        return trans.size();
    }
}


/*
执行用时：2 ms, 在所有 Java 提交中击败了75.06% 的用户
内存消耗：39.4 MB, 在所有 Java 提交中击败了36.65% 的用户
通过测试用例：82 / 82
*/
class Solution {
    public static final String[] morse = new String[]{".-","-...","-.-.","-..",".",
        "..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",
        ".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
    public int uniqueMorseRepresentations(String[] words) {

        Set<String> trans = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        for (String w: words) {
            sb.setLength(0);
            for (int i = 0; i < w.length(); i++) {
                sb.append(morse[w.charAt(i) - 'a']);
            }
            trans.add(sb.toString());
        }
        return trans.size();
    }
}
