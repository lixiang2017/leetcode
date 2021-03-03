/*
执行用时：4 ms, 在所有 C++ 提交中击败了96.36%的用户
内存消耗：7.7 MB, 在所有 C++ 提交中击败了71.84%的用户
*/

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> bits(num + 1);
        for (int i = 0; i <= num; i++) {
            bits[i] = __builtin_popcount(i);
        }
        return bits;
    }
};
