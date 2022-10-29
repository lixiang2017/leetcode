/*
执行用时：128 ms, 在所有 C# 提交中击败了96.54% 的用户
内存消耗：43.7 MB, 在所有 C# 提交中击败了24.49% 的用户
通过测试用例：57 / 57
*/

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> d = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; ++i)
        {
            if (d.ContainsKey(nums[i])) return new int[]{d[nums[i]], i};
            if (!d.ContainsKey(target - nums[i])) d.Add(target - nums[i], i);
        }
        return null;
    }
}
