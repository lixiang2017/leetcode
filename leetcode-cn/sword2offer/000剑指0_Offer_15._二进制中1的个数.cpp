/**
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：6 MB, 在所有 C++ 提交中击败了6.15% 的用户
 * **/


class Solution {
public:
    int hammingWeight(uint32_t n) {
        return __builtin_popcount(n);
    }
}; 

