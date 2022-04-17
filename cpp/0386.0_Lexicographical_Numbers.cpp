/*
执行用时：4 ms, 在所有 C++ 提交中击败了94.36% 的用户
内存消耗：10.7 MB, 在所有 C++ 提交中击败了76.55% 的用户
通过测试用例：26 / 26
*/
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        int num = 1;
        for (int i = 0; i < n; i++) {
            ans.push_back(num);
            if (num * 10 <= n) {
                num *= 10;
            } else {
                while (num % 10 == 9 || num + 1 > n) {
                    num /= 10;
                }
                num++;
            }
        }
        return ans;
    }
};
