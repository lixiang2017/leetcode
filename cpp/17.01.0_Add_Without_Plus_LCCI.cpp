/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.8 MB, 在所有 C++ 提交中击败了66.89% 的用户
通过测试用例：51 / 51
*/
class Solution {
public:
    int add(int a, int b) {
        uint32_t x_or = 0, carry = 0;
        while (b) {
            x_or = a ^ b;
            carry = (uint32_t)(a & b) << 1;
            a = x_or;
            b = carry;
        }
        return a;
    }
};
