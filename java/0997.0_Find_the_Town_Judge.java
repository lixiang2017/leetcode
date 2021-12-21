/*
执行用时：2 ms, 在所有 Java 提交中击败了99.21% 的用户
内存消耗：45.6 MB, 在所有 Java 提交中击败了93.00% 的用户
通过测试用例：92 / 92
*/

class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] in = new int[n + 1], out = new int[n + 1];
        for (int[] t: trust) {
            int a = t[0], b = t[1];
            in[b]++;
            out[a]++;
        }
        for (int i = 1; i < n + 1; i++) {
            if (in[i] == n - 1 && out[i] == 0) {
                return i;
            }
        }
        return -1;
    }
}


/*
执行用时：2 ms, 在所有 Java 提交中击败了99.21% 的用户
内存消耗：46 MB, 在所有 Java 提交中击败了45.77% 的用户
通过测试用例：92 / 92
*/
class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] in = new int[n + 1], out = new int[n + 1];
        for (int i = 0; i < trust.length; i++) {
            int a = trust[i][0], b = trust[i][1];
            in[b]++;
            out[a]++;
        }
        for (int i = 1; i < n + 1; i++) {
            if (in[i] == n - 1 && out[i] == 0) {
                return i;
            }
        }
        return -1;
    }
}
