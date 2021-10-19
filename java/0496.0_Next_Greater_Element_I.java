/*
Runtime: 7 ms, faster than 29.02% of Java online submissions for Next Greater Element I.
Memory Usage: 41.2 MB, less than 20.73% of Java online submissions for Next Greater Element I.
*/
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        for (int num: nums2) {
            while (!stack.empty() && stack.peek() < num)
                map.put(stack.pop(), num);
            stack.push(num);
        }
        for (int i = 0; i < nums1.length; i++)
            nums1[i] = map.getOrDefault(nums1[i], -1);
        return nums1;
    }
}
