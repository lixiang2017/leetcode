/*
one pass

执行用时：5 ms, 在所有 Java 提交中击败了56.85% 的用户
内存消耗：38.6 MB, 在所有 Java 提交中击败了28.97% 的用户
通过测试用例：152 / 152
*/

class Solution {
    public String getHint(String secret, String guess) {
        int[] diff = new int[10];
        int countA = 0, countB = 0;
        for (int i = 0; i < secret.length(); i++) {
            if (secret.charAt(i) == guess.charAt(i)) {
                countA++;
            } else {
                if (diff[guess.charAt(i) - '0']-- > 0) countB++;
                if (diff[secret.charAt(i) - '0']++ < 0) countB++;
            }
        }
        return countA + "A" + countB + "B";
    }
}
