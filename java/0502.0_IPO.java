/*
Runtime: 98 ms, faster than 88.80% of Java online submissions for IPO.
Memory Usage: 59.5 MB, less than 92.60% of Java online submissions for IPO.
*/
class Solution {
    class Project implements Comparable<Project> {
        int capital, profit;
        
        public Project(int capital, int profit) {
            this.capital = capital;
            this.profit = profit;
        }
        
        public int compareTo(Project project) {
            return capital - project.capital;
        }
    }
    
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        Project[] projects = new Project[n];
        for (int i = 0; i < n; i++) {
            projects[i] = new Project(capital[i], profits[i]);
        }
        Arrays.sort(projects);
        PriorityQueue<Integer> q = new PriorityQueue<Integer>(n, Collections.reverseOrder());
        int ptr = 0;
        for (int i = 0; i < k; i++) {
            while (ptr < n && projects[ptr].capital <= w) {
                q.add(projects[ptr++].profit);
            }
            if (q.isEmpty()) {
                break;
            }
            w += q.poll();
        }
        return w;
    }
}
