/*
Runtime: 7 ms, faster than 12.48% of C++ online submissions for Number of 1 Bits.
Memory Usage: 5.9 MB, less than 48.74% of C++ online submissions for Number of 1 Bits.
*/
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        while (n) {
            n &= (n - 1);
            ++ans;
        }
        return ans;
    }
};


/*
Runtime: 4 ms, faster than 36.04% of C++ online submissions for Number of 1 Bits.
Memory Usage: 5.8 MB, less than 96.65% of C++ online submissions for Number of 1 Bits.
*/
class Solution {
public:
    int hammingWeight(uint32_t n) {
        return __builtin_popcount(n);
    }
};


/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of 1 Bits.
Memory Usage: 6 MB, less than 48.74% of C++ online submissions for Number of 1 Bits.
*/
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        while (n) {
            if (n & 1) {
                ++ans;
            }
            n >>= 1;
        }
        return ans;
    }
};


/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of 1 Bits.
Memory Usage: 5.9 MB, less than 48.74% of C++ online submissions for Number of 1 Bits.
*/
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        for(int i = 0; i <= 32; ++i) {
            if (n & 1) {
                ++ans;
            }
            n >>= 1;
        }
        return ans;
    }
};






