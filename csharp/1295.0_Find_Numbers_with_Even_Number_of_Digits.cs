/*
执行用时：80 ms, 在所有 C# 提交中击败了61.11% 的用户
内存消耗：38.1 MB, 在所有 C# 提交中击败了88.89% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public int FindNumbers(int[] nums) {
        int ans = 0;
        foreach (int x in nums) {
            if (NumberOfDigits(x) % 2 == 0)
            {
                ans++;
            }
        }
        return ans;
    }

    private int NumberOfDigits(int x)
    {
        int res = 0;
        while (x != 0)
        {
            ++res;
            x /= 10;
        }
        return res;
    }
}


/*
执行用时：80 ms, 在所有 C# 提交中击败了61.11% 的用户
内存消耗：39 MB, 在所有 C# 提交中击败了5.55% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public int FindNumbers(int[] nums) {
        return nums.Where(x => x.ToString().Length % 2 == 0).Count();
    }
}


/*
执行用时：88 ms, 在所有 C# 提交中击败了33.33% 的用户
内存消耗：39 MB, 在所有 C# 提交中击败了5.55% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public int FindNumbers(int[] nums) {
        return nums.ToList().FindAll(k => k.ToString().Length % 2 == 0).Count();
    }
}

/*
执行用时：88 ms, 在所有 C# 提交中击败了33.33% 的用户
内存消耗：38.9 MB, 在所有 C# 提交中击败了5.55% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public int FindNumbers(int[] nums) {
        return nums.ToList().Where(k => k.ToString().Length % 2 == 0).Count();
    }
}


/*
执行用时：100 ms, 在所有 C# 提交中击败了16.67% 的用户
内存消耗：38.6 MB, 在所有 C# 提交中击败了44.44% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public int FindNumbers(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.Length; ++i)
        {
            if (nums[i].ToString().Length % 2 == 0) ans++;
        }
        return ans;
    }
}



/*
执行用时：80 ms, 在所有 C# 提交中击败了61.11% 的用户
内存消耗：38.7 MB, 在所有 C# 提交中击败了33.33% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public int FindNumbers(int[] nums) {
        int ans = 0;
        string s;
        for (int i = 0; i < nums.Length; ++i)
        {
            s = Convert.ToString(nums[i]);
            if ((s.Length & 1) == 0) ++ans;
        }
        return ans;
    }
}

