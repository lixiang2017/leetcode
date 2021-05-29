/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了6.13% 的用户
*/

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && __builtin_popcount(n) == 1;
    }
};


/*
执行用时：4 ms, 在所有 C++ 提交中击败了43.14% 的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了6.13% 的用户
*/
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && 0 == (n & (n - 1));
    }
};


/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了16.15% 的用户
*/
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && n == (n & -n);
    }
};