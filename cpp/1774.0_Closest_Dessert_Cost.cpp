/*
执行用时：12 ms, 在所有 C++ 提交中击败了83.66% 的用户
内存消耗：9.5 MB, 在所有 C++ 提交中击败了63.86% 的用户
通过测试用例：89 / 89
*/
class Solution {
public:
    int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int target) {
        bitset<20005> f;
        for (auto x: baseCosts) f[x] = 1;
        for (auto x: toppingCosts) f |= (f << x) | (f << (x * 2));
        int ans = -20000;
        for (int x = 0; x <= 20000; ++x)
            if (f[x] && abs(x - target) < abs(ans - target))
                ans = x;
        return ans;
    }
};
