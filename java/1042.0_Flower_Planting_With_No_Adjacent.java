/*
执行用时：11 ms, 在所有 Java 提交中击败了67.20% 的用户
内存消耗：51 MB, 在所有 Java 提交中击败了17.21% 的用户
通过测试用例：51 / 51
*/
class Solution {
    public int[] gardenNoAdj(int n, int[][] paths) {
        List<Integer> g[] = new ArrayList[n];
        Arrays.setAll(g, index -> new ArrayList<>());
        for (var e: paths) {
            int x = e[0] - 1, y = e[1] - 1;
            g[x].add(y);
            g[y].add(x);
        }
        var color = new int[n];
        for (int i = 0; i < n; ++i) {
            int mask = 1;
            for (var j : g[i]) {
                mask |= 1 << color[j];
            }
            color[i] = Integer.numberOfTrailingZeros(~mask);
        }
        return color;
    }
}


/*
执行用时：16 ms, 在所有 Java 提交中击败了51.08% 的用户
内存消耗：50.1 MB, 在所有 Java 提交中击败了47.31% 的用户
通过测试用例：51 / 51
*/
class Solution {
    public int[] gardenNoAdj(int n, int[][] paths) {
        List<Integer> g[] = new ArrayList[n];
        Arrays.parallelSetAll(g, index -> new ArrayList<>());
        for (var e: paths) {
            int x = e[0] - 1, y = e[1] - 1;
            g[x].add(y);
            g[y].add(x);
        }
        var color = new int[n];
        for (int i = 0; i < n; ++i) {
            int mask = 1;
            for (var j : g[i]) {
                mask |= 1 << color[j];
            }
            color[i] = Integer.numberOfTrailingZeros(~mask);
        }
        return color;
    }
}
