/*
执行用时：124 ms, 在所有 C++ 提交中击败了84.02% 的用户
内存消耗：56 MB, 在所有 C++ 提交中击败了41.20% 的用户
通过测试用例：68 / 68
*/
class RecentCounter {
private:
    queue<int> q;
public:
    RecentCounter() {
    }
    
    int ping(int t) {
        q.push(t);
        while(q.front() < t - 3000) {
            q.pop();
        }
        return q.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
 