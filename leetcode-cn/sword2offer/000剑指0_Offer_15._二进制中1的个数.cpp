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



/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了12.89% 的用户
*/

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        for (int i = 0; i < 32; ++i)
        {
            if (n & (1 << i))
                cnt ++;
        }
        return cnt;
    }
};






/*
C

执行用时：0 ms, 在所有 C 提交中击败了100.00% 的用户
内存消耗：5.4 MB, 在所有 C 提交中击败了20.02% 的用户
*/
int hammingWeight(uint32_t n) {
    int cnt = 0;
    for (int i = 0; i < 32; ++i) {
        if (n & (1u << i)) {
            cnt ++;
        }
    }
    return cnt;
}



 
