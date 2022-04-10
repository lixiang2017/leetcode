/*
Runtime: 14 ms, faster than 72.22% of Java online submissions for Top K Frequent Elements.
Memory Usage: 50.6 MB, less than 40.78% of Java online submissions for Top K Frequent Elements.
*/
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // O(1) time
        if (k == nums.length) {
            return nums;
        }
        
        // 1. build hash map: character and how often it appears
        // O(N) time
        Map<Integer, Integer> freq = new HashMap();
        for (int x: nums){
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }
        
        // init heap 'the less frequent element first'
        Queue<Integer> h = new PriorityQueue<>((x1, x2) -> freq.get(x1) -freq.get(x2));
        
        // 2. keep k top frequent elements in the heap
        // O(Nlogk) < O(NlogN) time
        for (int x: freq.keySet()) {
            h.add(x);
            if (h.size() > k) h.poll();
        }
        
        // 3. build an output array
        // O(klogK) time
        int[] top = new int[k];
        for (int i = k - 1; i >= 0; --i) {
            top[i] = h.poll();
        }
        return top;
    }
}