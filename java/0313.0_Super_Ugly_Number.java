/*
PriorityQueue + HashSet
Time: O(MNlogMN)
Space: O(2MN)

执行用时：491 ms, 在所有 Java 提交中击败了18.45% 的用户
内存消耗：156.6 MB, 在所有 Java 提交中击败了22.74% 的用户
*/
class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        Set<Long> seen = new HashSet<Long>();
        PriorityQueue<Long> h = new PriorityQueue<Long>();
        seen.add(1L);
        h.offer(1L);
        int ugly = 0;
        for (int i = 0; i < n; i++) {
            long curr = h.poll();
            ugly = (int) curr;
            for (int prime: primes) {
                long next = curr * prime;
                if (seen.add(next)) {
                    h.offer(next);
                }
            }
        }
        return ugly;
    }
}
