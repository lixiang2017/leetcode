/*
执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：35.4 MB, 在所有 Java 提交中击败了6.83% 的用户
通过测试用例：17 / 17
*/
class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int pig = 0;
        int round = minutesToTest / minutesToDie + 1;
        while (Math.pow(round, pig) < buckets) {
            pig++;
        }
        return pig;
    }
}
