/*
执行用时：1 ms, 在所有 Java 提交中击败了99.32% 的用户
内存消耗：41.2 MB, 在所有 Java 提交中击败了76.82% 的用户
通过测试用例：57 / 57
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];
        Map<Integer, Integer> m = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (m.containsKey(target - nums[i])) {
                indices[0] = m.get(target - nums[i]);
                indices[1] = i;
                return indices;
            }
            m.put(nums[i], i);
        }
        return indices;
    }
}


/*
执行用时：2 ms, 在所有 Java 提交中击败了71.80% 的用户
内存消耗：41.6 MB, 在所有 Java 提交中击败了28.91% 的用户
通过测试用例：57 / 57
*/
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];
        Map<Integer, Integer> m = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (m.containsKey(nums[i])) {
                indices[0] = m.get(nums[i]);
                indices[1] = i;
                return indices;
            }
            m.put(target - nums[i], i);
        }
        return indices;
    }
}
