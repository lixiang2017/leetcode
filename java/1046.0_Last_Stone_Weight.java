/*
T: O((N^2)*logN)

执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：38.9 MB, 在所有 Java 提交中击败了32.61% 的用户
通过测试用例：70 / 70
*/
class Solution {
    public int lastStoneWeight(int[] stones) {
        int n = stones.length;
        if (n == 2)
            return Math.abs(stones[0] - stones[1]);
        if (n == 1)
            return stones[0];
        Arrays.sort(stones);
        if (stones[n - 3] == 0)
            return stones[n - 1] - stones[n - 2];
        stones[n - 1] -= stones[n - 2];
        stones[n - 2] = 0;
        return lastStoneWeight(stones);
    }
}
