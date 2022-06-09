/*
执行用时：102 ms, 在所有 Java 提交中击败了28.72% 的用户
内存消耗：42 MB, 在所有 Java 提交中击败了57.43% 的用户
通过测试用例：98 / 98
*/
class MyCalendarThree {
    private TreeMap<Integer, Integer> cnt = new TreeMap<Integer, Integer>();
    public MyCalendarThree() {

    }
    
    public int book(int start, int end) {
        int ans = 0, presum = 0;
        cnt.put(start, cnt.getOrDefault(start, 0) + 1);
        cnt.put(end, cnt.getOrDefault(end, 0) - 1);
        for (Map.Entry<Integer, Integer> entry : cnt.entrySet()) {
            int freq = entry.getValue();
            presum += freq;
            ans = Math.max(ans, presum);
        }
        return ans;
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */

 