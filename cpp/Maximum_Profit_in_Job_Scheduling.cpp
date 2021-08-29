/*
You are here!
Your runtime beats 37.17 % of cpp submissions.
You are here!
Your memory usage beats 51.53 % of cpp submissions.
*/
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        vector<Job> jobs;
        for (int i = 0; i < startTime.size(); i++) {
            jobs.push_back(Job(startTime[i], endTime[i], profit[i]));
        }
        sort(jobs.begin(), jobs.end());
        map<int, int> dp;
        int ans = 0;
        for (int i = 0; i < jobs.size(); i++) {
            Job cur = jobs[i];
            int afterCurEndMaxProfit = dp.lower_bound(cur.end) -> second;
            dp[cur.start] = max(dp[cur.start], afterCurEndMaxProfit + cur.profit);
            dp[cur.start] = max(ans, dp[cur.start]);
            ans = max(dp[cur.start], ans);
        }
        return ans;
    }

private:
    struct Job {
        Job(int start, int end, int profit):
            start(start), end(end), profit(profit) {};
        int start;
        int end;
        int profit;
        bool operator < (const Job& rhs) const {
            return  start > rhs.start;
        }
    };
};