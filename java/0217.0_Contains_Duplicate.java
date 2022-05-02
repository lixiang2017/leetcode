/*
执行用时：14 ms, 在所有 Java 提交中击败了48.56% 的用户
内存消耗：52.7 MB, 在所有 Java 提交中击败了61.43% 的用户
通过测试用例：70 / 70
*/
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<Integer>();
        for (int x: nums)
            s.add(x);
        return s.size() < nums.length ? true: false;
    }
}


/*
执行用时：5 ms, 在所有 Java 提交中击败了91.02% 的用户
内存消耗：49.7 MB, 在所有 Java 提交中击败了77.38% 的用户
通过测试用例：70 / 70
*/
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int num: nums) {
            if (s.add(num) == false) {
                return true;
            }
        }
        return false;
    }
}


/*
执行用时：20 ms, 在所有 Java 提交中击败了13.35% 的用户
内存消耗：55 MB, 在所有 Java 提交中击败了19.64% 的用户
通过测试用例：70 / 70
*/
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1])
                return true;
        }
        return false;
    }
}


