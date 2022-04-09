/*
执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：40.8 MB, 在所有 Java 提交中击败了49.24% 的用户
通过测试用例：37 / 37
*/
class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        int d1 = 0, d2 = 0;
        int l = Math.min(start, destination);
        int r = Math.max(start, destination);
        for (int i = 0; i < distance.length; i++) {
            if (i >= l && i < r) {
                d1 += distance[i];
            } else {
                d2 += distance[i];
            }
        }
        return Math.min(d1, d2);
    }
}
