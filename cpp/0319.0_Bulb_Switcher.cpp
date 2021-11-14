/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.8 MB, 在所有 C++ 提交中击败了53.01% 的用户
通过测试用例：35 / 35
*/

class Solution {
public:
    int bulbSwitch(int n) {
        return (int)(sqrt(n));
    }
};



/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.8 MB, 在所有 C++ 提交中击败了78.40% 的用户
通过测试用例：35 / 35
*/

class Solution {
public:
    int bulbSwitch(int n) {
        return static_cast<int>(sqrt(n));
    }
};
