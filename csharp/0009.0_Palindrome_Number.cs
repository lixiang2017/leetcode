/*
执行用时：36 ms, 在所有 C# 提交中击败了83.69% 的用户
内存消耗：28.6 MB, 在所有 C# 提交中击败了97.02% 的用户
通过测试用例：11510 / 11510
*/
public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0) return false;
        int back = 0, xx = x;
        while (x != 0) {
            back = back * 10 + x % 10;
            x /= 10;
        }
        return back == xx;
    }
}

/*
执行用时：44 ms, 在所有 C# 提交中击败了46.22% 的用户
内存消耗：28.6 MB, 在所有 C# 提交中击败了95.76% 的用户
通过测试用例：11510 / 11510
*/
public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        int revertedNumber = 0;
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        return x == revertedNumber || x == revertedNumber / 10;
    }
}