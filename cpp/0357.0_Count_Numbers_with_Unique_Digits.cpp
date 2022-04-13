/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.7 MB, 在所有 C++ 提交中击败了99.61% 的用户
通过测试用例：9 / 9
*/
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int ans = 1, init = 9, i = 1;
        while (i <= n) {
            ans += init;
            init *= (9 - i + 1);
            i += 1;
        }
        return ans;
    }
};


/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.7 MB, 在所有 C++ 提交中击败了96.99% 的用户
通过测试用例：9 / 9
*/
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
       int ans = 0;
        switch(n) {
            case 8: ans += 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3;
            case 7: ans += 9 * 9 * 8 * 7 * 6 * 5 * 4;
            case 6: ans += 9 * 9 * 8 * 7 * 6 * 5;
            case 5: ans += 9 * 9 * 8 * 7 * 6;
            case 4: ans += 9 * 9 * 8 * 7;
            case 3: ans += 9 * 9 * 8;
            case 2: ans += 9 * 9;
            case 1: ans += 9;
            case 0: ans += 1;
        }
        return ans;
    }
};
