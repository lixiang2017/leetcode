/*
执行用时：8 ms, 在所有 C++ 提交中击败了25.16% 的用户
内存消耗：9.4 MB, 在所有 C++ 提交中击败了18.71% 的用户
通过测试用例：84 / 84
*/
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int n = arr.size();
        for (int i = 0; i < n; i++) {
            if (arr[i] - i - 1 >= k) {
                return k + i;
            }
        }
        return k + n;
    }
};


/*
binary search

执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：9.2 MB, 在所有 C++ 提交中击败了85.55% 的用户
通过测试用例：84 / 84
*/
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int l = 0, r = arr.size() - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (arr[mid] - mid - 1 >= k) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return k + r + 1;
    }
};

/*
binary search

执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：9.2 MB, 在所有 C++ 提交中击败了76.39% 的用户
通过测试用例：84 / 84
*/
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int l = 0, r = arr.size() - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (arr[mid] - mid - 1 >= k) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return k + l;
    }
};
