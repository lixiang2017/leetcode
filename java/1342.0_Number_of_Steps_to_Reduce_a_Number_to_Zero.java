/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 41.4 MB, less than 23.39% of Java online submissions for Number of Steps to Reduce a Number to Zero.
*/
class Solution {
    public int numberOfSteps(int num) {
        int step = 0;
        while (num != 0) {
            if ((num & 1) != 0) {
                --num;
            } else {
                num >>= 1;
            }
            ++step;
        }
        return step;        
    }
}
