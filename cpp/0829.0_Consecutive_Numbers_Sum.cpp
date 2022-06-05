/*
执行用时：4 ms, 在所有 C++ 提交中击败了68.54% 的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了9.22% 的用户
通过测试用例：170 / 170
*/
class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int ans = 0;
        for (int i = 1; n > 0; n -= i++) {
            ans += (n % i == 0);
        }
        return ans;
    }
};



/*
执行用时：4 ms, 在所有 C++ 提交中击败了68.54% 的用户
内存消耗：5.7 MB, 在所有 C++ 提交中击败了92.18% 的用户
通过测试用例：170 / 170
*/
class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int ans = 0;
        for (int i = 1; n > 0; n -= i++) {
            if (0 == n % i) { 
                ans++;
            }
        }
        return ans;
    }
};


/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了19.64% 的用户
通过测试用例：170 / 170
*/
class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int ans = 0, i = 1;
        while (n > 0) {
            ans += (n % i == 0);
            n -= i++;
        }
        return ans;
    }
};



