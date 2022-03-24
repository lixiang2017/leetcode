/*
sort + two pointers
T: O(NlogN + N)
S: O(logN), for quick sort

Runtime: 129 ms, faster than 30.49% of C++ online submissions for Boats to Save People.
Memory Usage: 41.9 MB, less than 91.53% of C++ online submissions for Boats to Save People.
*/

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int i = 0, j = people.size() - 1;
        int ans = 0;
        while (i <= j) {
            ans++;
            if (people[i] + people[j] <= limit)
                i++;
            j--;
        }
        return ans;
    }
};
