/*
T: O(N^2)
S: O(N)

执行用时：44 ms, 在所有 C++ 提交中击败了35.85% 的用户
内存消耗：10.7 MB, 在所有 C++ 提交中击败了82.26% 的用户
通过测试用例：44 / 44
*/
class Section {
public:
    int left;
    int right;
    int height;

    Section(int left_, int right_, int height_) : left(left_), right(right_), height(height_) {}

    bool isOverlap(int start, int end) {
        return (start >= left && start <= right) || (end >= left && end <= right) || (start < left && end > right);
    }
};

class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        vector<Section> sections;
        int n = positions.size(), max_height = 0;
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            int sl = positions[i][1], height = sl;
            int start = positions[i][0], end = start + sl - 1;
            for (Section & section : sections) {
                if (section.isOverlap(start, end)) {
                    height = max(height, section.height + sl);
                }
            }
            sections.push_back(Section(start, end, height));
            max_height = max(max_height, height);
            ans[i] = max_height;
        }
        return ans;
    }
};
