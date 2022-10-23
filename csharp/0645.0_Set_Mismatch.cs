/*
sort

执行用时：156 ms, 在所有 C# 提交中击败了74.49% 的用户
内存消耗：49.6 MB, 在所有 C# 提交中击败了76.53% 的用户
通过测试用例：49 / 49
*/

public class Solution {
    public int[] FindErrorNums(int[] nums) {
        int[] errorNums = new int[2];
        int n = nums.Length;
        Array.Sort(nums);
        int prev = 0;
        for (int i = 0; i < n; ++i) {
            int curr = nums[i];
            if (curr == prev) {
                errorNums[0] = prev;
            } else if (curr - prev > 1) {
                errorNums[1] = prev + 1;
            }
            prev = curr;
        }
        if (nums[n - 1] != n) {
            errorNums[1] = n;
        }
        return errorNums;
    }
}



/*
执行用时：164 ms, 在所有 C# 提交中击败了52.04% 的用户
内存消耗：49.6 MB, 在所有 C# 提交中击败了79.59% 的用户
通过测试用例：49 / 49
*/
public class Solution {
    public int[] FindErrorNums(int[] nums) {
        int[] errorNums = new int[2];
        int n = nums.Length;
        Array.Sort(nums);
        int prev = 0;
        for (int i = 0; i < n; ++i) {
            int curr = nums[i];
            if (curr == prev) {
                errorNums[0] = prev;
            } else if (curr - prev > 1) {
                errorNums[1] = prev + 1;
            }
            if (errorNums[0] != 0 && errorNums[1] != 0) {
                return errorNums;
            }
            prev = curr;
        }
        if (nums[n - 1] != n) {
            errorNums[1] = n;
        }
        return errorNums;
    }
}



/*
执行用时：188 ms, 在所有 C# 提交中击败了16.33% 的用户
内存消耗：51.2 MB, 在所有 C# 提交中击败了40.82% 的用户
通过测试用例：49 / 49
*/
public class Solution {
    public int[] FindErrorNums(int[] nums) {
        int[] errorNums = new int[2];
        int n = nums.Length;
        Dictionary<int, int> d = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!d.ContainsKey(x)) {
                d.Add(x, 1);
            } else {
                d[x]++;
            }
        }
        for (int i = 1; i <= n; ++i) {
            int count = 0;
            d.TryGetValue(i, out count);
            if (count == 2) {
                errorNums[0] = i;
            } else if (count == 0) {
                errorNums[1] = i;
            }
        }
        return errorNums;
    }
}


/*
xor, 把数字按照 lowbit 分成两类
T: O(5 * N)
S: O(1)

执行用时：156 ms, 在所有 C# 提交中击败了74.49% 的用户
内存消耗：49.3 MB, 在所有 C# 提交中击败了98.98% 的用户
通过测试用例：49 / 49
*/
public class Solution {
    public int[] FindErrorNums(int[] nums) {
        int n = nums.Length;
        int xor = 0;
        foreach (int x in nums) {
            xor ^= x;
        }
        for (int i = 1; i <= n; ++i) {
            xor ^= i;
        }
        int lowbit = xor & -xor;
        int num1 = 0, num2 = 0;
        foreach (int x in nums) {
            if (0 == (x & lowbit)) {
                num1 ^= x;
            } else {
                num2 ^= x;
            }
        }
        for (int i = 1; i <= n; ++i) {
            if (0 == (i & lowbit)) {
                num1 ^= i;
            } else {
                num2 ^= i;
            }
        }
        foreach (int x in nums) {
            if (x == num1) {
                return new int[]{num1, num2};
            }
        }
        return new int[]{num2, num1};
    }
}
