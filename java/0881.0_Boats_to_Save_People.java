/*
sort + two pointers
T: O(NlogN + N)
S: O(logN), for quick sort

Runtime: 20 ms, faster than 61.45% of Java online submissions for Boats to Save People.
Memory Usage: 65.9 MB, less than 14.62% of Java online submissions for Boats to Save People.
*/

class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1;
        int ans = 0;
        while (i <= j) {
            ans++;
            if (people[i] + people[j] <= limit)
                i++;
            j--;
        }
        
        return ans;
    }
}
