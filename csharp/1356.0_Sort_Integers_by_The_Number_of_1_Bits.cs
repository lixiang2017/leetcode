/*
先计算1的个数，取个范围外的100000*（1的个数）改变原数组，进行排序。最后取余还原数组

执行用时：140 ms, 在所有 C# 提交中击败了58.33% 的用户
内存消耗：43.5 MB, 在所有 C# 提交中击败了75.00% 的用户
通过测试用例：77 / 77

ref:
https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/solution/jie-by-long-yu-8-2/
*/

public class Solution {
    public int[] SortByBits(int[] arr) {
        for (int i = 0; i < arr.Length; i++)
        {
            arr[i] += bitCount(arr[i]) * 100000;
        }
        Array.Sort(arr);
        for (int i = 0; i < arr.Length; i++)
        {
            arr[i] %= 100000;
        }
        return arr;
    }

    private int bitCount(int x)
    {
        int res = 0;
        while (x != 0)
        {
            res += (x % 2);
            x >>= 1;
        }
        return res;
    }
}


/*
执行用时：144 ms, 在所有 C# 提交中击败了41.67% 的用户
内存消耗：43.4 MB, 在所有 C# 提交中击败了87.50% 的用户
通过测试用例：77 / 77
*/
public class Solution {
    public int[] SortByBits(int[] arr) {
        Array.Sort(arr, (x, y) => {
            var bx = BitCount(x);
            var by = BitCount(y);
            return (bx == by) ? x.CompareTo(y) : bx.CompareTo(by);
        });
        return arr;
    }

    private int BitCount(int x)
    {
        int res = 0;
        while (x > 0)
        {
            if ((x & 1) == 1) res++;
            x >>= 1;
        }
        return res;
    }
}


/*
执行用时：148 ms, 在所有 C# 提交中击败了20.83% 的用户
内存消耗：46.4 MB, 在所有 C# 提交中击败了8.33% 的用户
通过测试用例：77 / 77
*/
public class Solution {
    public int[] SortByBits(int[] arr) {
        int [] bit = new int [10001];
        for (int i = 0; i < arr.Length; i++)
        {
            bit[arr[i]] = BitCount(arr[i]);
        }

        Array.Sort(arr, (x, y) => {
            if (bit[x] != bit[y])
            {
                return bit[x] - bit[y];
            }
            else
            {
                return x - y;
            }
        });
        return arr;
    }

    private int BitCount(int x)
    {
        int res = 0;
        while (x > 0)
        {
            if ((x & 1) == 1) res++;
            x >>= 1;
        }
        return res;
    }
}


/*
ref:
https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/solution/c-linqfei-chang-hao-yong-by-rickychu/

执行用时：160 ms, 在所有 C# 提交中击败了12.50% 的用户
内存消耗：45.1 MB, 在所有 C# 提交中击败了37.50% 的用户
通过测试用例：77 / 77
*/
public class Solution {
    public int[] SortByBits(int[] arr) {
        return arr.OrderBy(x => Convert.ToString(x, 2).Count(a => a == '1')).ThenBy(x => x).ToArray();
    }
}
