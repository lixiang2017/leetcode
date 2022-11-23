/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.7 MB, 在所有 C++ 提交中击败了91.89% 的用户
通过测试用例：70 / 70
*/
class Solution {
    typedef long long LL;
    const int MOD = 1e9 +7;
public:
    int nthMagicalNumber(int n, int a, int b) {
        int lcm = a / gcd(a, b) * b;
        LL l = 0;
        LL r = n * 1LL * min(a, b);
        while (l < r) {
            LL mid = (l + r) >> 1;
            LL cnt = mid / a + mid / b - mid / lcm;
            if (cnt >= n) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return r % MOD;
    }

private:
    int gcd(int a, int b) {
        return b ? gcd(b, a % b) : a;
    }
};
