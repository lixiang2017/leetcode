/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：7.7 MB, 在所有 C++ 提交中击败了87.14% 的用户
通过测试用例：80 / 80
*/
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int highest = 0, altitude = 0;
        for (auto &g : gain) {
            altitude += g;
            highest = max(highest, altitude);
        }
        return highest;
    }
};
