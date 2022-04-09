/*
heap
T: O(NlogN + Mlogk)
S: O(N)

Runtime: 17 ms, faster than 80.82% of Java online submissions for Kth Largest Element in a Stream.
Memory Usage: 52.7 MB, less than 35.76% of Java online submissions for Kth Largest Element in a Stream.
*/
class KthLargest {
    private static int k;
    private PriorityQueue<Integer> heap;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        heap = new PriorityQueue<>();
        for (int x: nums) {
            heap.offer(x);
        }
        while (heap.size() > k) {
            heap.poll();
        }
    }
    
    public int add(int val) {
        heap.offer(val);
        if (heap.size() > k) {
            heap.poll();
        }
        return heap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */



/*
add

Runtime: 11 ms, faster than 97.45% of Java online submissions for Kth Largest Element in a Stream.
Memory Usage: 46.6 MB, less than 86.19% of Java online submissions for Kth Largest Element in a Stream.
*/

class KthLargest {
    private static int k;
    private PriorityQueue<Integer> heap;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        heap = new PriorityQueue<>();
        for (int x: nums) {
            heap.add(x);
        }
        while (heap.size() > k) {
            heap.poll();
        }
    }
    
    public int add(int val) {
        heap.add(val);
        if (heap.size() > k) {
            heap.poll();
        }
        return heap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */

