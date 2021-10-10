/*
执行用时：8 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：39.1 MB, 在所有 Java 提交中击败了100.00% 的用户
通过测试用例：288 / 288
*/

class Solution {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        Set<Integer> us1 = new HashSet<>();
        for (int x: nums1) us1.add(x);
        Set<Integer> us2 = new HashSet<>();
        for (int x: nums2) us2.add(x);
        Set<Integer> us3 = new HashSet<>();
        for (int x: nums3) us3.add(x);

        Set<Integer> us = new HashSet<>();
        us.addAll(us1);
        us.addAll(us2);
        us.addAll(us3);

        List<Integer> ans = new ArrayList<>();
        for (int x: us) {
            int f1 = us1.contains(x) == true ? 1 : 0;
            int f2 = us2.contains(x) == true ? 1 : 0;
            int f3 = us3.contains(x) == true ? 1 : 0;
            if (f1 + f2 + f3 >= 2) {
                ans.add(x);
            }
        }
        return ans;
    }
}
