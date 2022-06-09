/*
执行用时：96 ms, 在所有 C++ 提交中击败了66.55% 的用户
内存消耗：25.8 MB, 在所有 C++ 提交中击败了31.38% 的用户
通过测试用例：98 / 98
*/
class MyCalendarThree {
public:
    MyCalendarThree() {

    }
    
    int book(int start, int end) {
        int ans = 0, presum = 0;
        cnt[start]++;
        cnt[end]--;
        for (auto &[_, freq] : cnt) {
            presum += freq;
            ans = max(ans, presum);
        }
        return ans;
    }
private:
    map<int, int> cnt;
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(start,end);
 */
 