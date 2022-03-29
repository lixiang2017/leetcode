/*
T: O(1)
S: O(1)

执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了15.69% 的用户
通过测试用例：500 / 500
*/
class Solution {
public:
    int trailingZeroes(int n) {
        return n/5 + n/25 + n/125 + n/625 + n/3125;
    }
};


/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.8 MB, 在所有 C++ 提交中击败了50.40% 的用户
通过测试用例：500 / 500
*/
class Solution {
public:
    int trailingZeroes(int n) {
        return n < 5 ? 0: n / 5 + trailingZeroes(n / 5);
    }
};

