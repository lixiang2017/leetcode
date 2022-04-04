/*
binary search, T: O(logN), S: O(1)

执行用时：24 ms, 在所有 C++ 提交中击败了11.35% 的用户
内存消耗：15.4 MB, 在所有 C++ 提交中击败了73.23% 的用户
通过测试用例：165 / 165
*/
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int len = letters.size();
        int l = 0, r = len - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (target < letters[mid])
                r = mid - 1;
            else
                l = mid + 1;
        }
        return letters[l % len];
    }
};


/*
执行用时：8 ms, 在所有 C++ 提交中击败了97.62% 的用户
内存消耗：15.4 MB, 在所有 C++ 提交中击败了64.13% 的用户
通过测试用例：165 / 165
*/
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int idx = upper_bound(letters.begin(), letters.end(), target) - letters.begin();
        return letters[idx % letters.size()];
    }
};


/*
执行用时：12 ms, 在所有 C++ 提交中击败了79.96% 的用户
内存消耗：15.3 MB, 在所有 C++ 提交中击败了92.05% 的用户
通过测试用例：165 / 165
*/
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int n = letters.size();
        int l = 0, r = n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (letters[mid] <= target)
                l = mid + 1;
            else
                r = mid;
        }
        return letters[l % n];
    }
};

