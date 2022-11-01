/*
执行用时：188 ms, 在所有 C# 提交中击败了10.26% 的用户
内存消耗：44.3 MB, 在所有 C# 提交中击败了5.13% 的用户
通过测试用例：103 / 103
*/
public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        return nums.Select(t => nums.Count(o => t > o)).ToArray();   
    }
}


/*
执行用时：144 ms, 在所有 C# 提交中击败了53.85% 的用户
内存消耗：42.9 MB, 在所有 C# 提交中击败了30.77% 的用户
通过测试用例：103 / 103
*/
public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        int size = nums.Length;
        int[] ans = new int[size];
        for (int i = 0; i < size; i++)
        {
            for (int j = 0; j < size; j++)
            {
                if (nums[i] > nums[j])
                {
                    ans[i]++;
                }
            }
        }
        return ans;
    }
}
