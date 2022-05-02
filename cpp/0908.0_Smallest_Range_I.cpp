/*
执行用时：12 ms, 在所有 C++ 提交中击败了83.09% 的用户
内存消耗：15 MB, 在所有 C++ 提交中击败了52.19% 的用户
通过测试用例：68 / 68
*/

class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        auto mm = minmax_element(nums.begin(), nums.end());
        return max(0, abs(*mm.first - *mm.second) - 2 * k);
    }
};



/*
执行用时：16 ms, 在所有 C++ 提交中击败了49.48% 的用户
内存消耗：15.1 MB, 在所有 C++ 提交中击败了45.30% 的用户
通过测试用例：68 / 68
*/
class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        std::vector<int>::iterator max_it = max_element(nums.begin(), nums.end());
        std::vector<int>::iterator min_it = min_element(nums.begin(), nums.end());
        return max(0, *max_it - *min_it - 2 * k);
    }
};


/*
执行用时：8 ms, 在所有 C++ 提交中击败了96.45% 的用户
内存消耗：15 MB, 在所有 C++ 提交中击败了53.65% 的用户
通过测试用例：68 / 68
*/
class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        vector<int>::iterator max_it = max_element(nums.begin(), nums.end());
        vector<int>::iterator min_it = min_element(nums.begin(), nums.end());
        return max(0, *max_it - *min_it - 2 * k);
    }
};


/*
执行用时：16 ms, 在所有 C++ 提交中击败了49.48% 的用户
内存消耗：15.1 MB, 在所有 C++ 提交中击败了37.79% 的用户
通过测试用例：68 / 68
*/
class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        int maxx = *max_element(nums.begin(), nums.end());
        int minx = *min_element(nums.begin(), nums.end());
        return max(0, maxx - minx - 2 * k);
    }
};






