/*
max heap + simulation
T: O(N + NlogN)
S: O(N)

Runtime: 4 ms, faster than 37.54% of C++ online submissions for Last Stone Weight.
Memory Usage: 7.6 MB, less than 78.96% of C++ online submissions for Last Stone Weight.
*/
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq(stones.begin(), stones.end());
        while (pq.size() > 1) {
            int first = pq.top();
            pq.pop();
            int second = pq.top();
            pq.pop();
            if (first != second) {
                pq.push(first - second);
            }
        }
        return pq.empty() ? 0: pq.top();
    }
};
