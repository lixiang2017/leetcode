/*
iteration

执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.8 MB, 在所有 C++ 提交中击败了88.08% 的用户
通过测试用例：304 / 304
*/

class Solution {
public:
    double myPow(double x, int n) {
        double ans = 1.0;
        for (int i = n; i != 0; i /= 2) {
            if (i & 1) {
                ans *= x;
            }
            x *= x;
        }
        return n < 0 ? 1 / ans : ans;
    }
};


/*
recursion

执行用时：4 ms, 在所有 C++ 提交中击败了32.89% 的用户
内存消耗：5.8 MB, 在所有 C++ 提交中击败了70.16% 的用户
通过测试用例：304 / 304
*/
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) { return 1.; }
        if (n == -1) { return 1. / x; }
        if (n & 1) { return myPow(x * x, n >> 1) * x; }
        return myPow(x * x, n >> 1);
    }
};


/*
recursion

执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.8 MB, 在所有 C++ 提交中击败了67.32% 的用户
通过测试用例：304 / 304
*/
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) { return 1.; }
        if (n == 1) { return x; }
        if (n == -1) { return 1. / x; }
        double d1 = myPow(x, n % 2);
        double d2 = myPow(x, n / 2);
        d2 *= d2 * d1;
        return d2;
    }
};

/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.7 MB, 在所有 C++ 提交中击败了94.50% 的用户
通过测试用例：304 / 304
*/
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) { return 1.; }
        if (n == 1) { return x; }
        if (n == -1) { return 1. / x; }
        double rest = myPow(x, n % 2);
        double half = myPow(x, n / 2);
        return half * half * rest;
    }
};


