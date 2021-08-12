/*
TreeMap
Time: O(NlogN)
Space: O(N)

You are here!
Your runtime beats 72.79 % of java submissions.
You are here!
Your memory usage beats 27.68 % of java submissions.
*/
class Solution {
    public boolean canReorderDoubled(int[] arr) {
        Map<Integer, Integer> count = new TreeMap<>();
        for (int a: arr)
            count.put(a, count.getOrDefault(a, 0) + 1);
        for (int x: count.keySet()) {
            if (count.get(x) == 0) continue;
            int want = x < 0 ? x / 2 : x * 2;
            if (x < 0 && x % 2 != 0 || count.get(x) > count.getOrDefault(want, 0))
                return false;
            count.put(want, count.get(want) - count.get(x));
        }
        return true;
    }
}




/*
HashMap
Time: O(NlogN)
Space: O(N)

You are here!
Your runtime beats 15.27 % of java submissions
You are here!
Your memory usage beats 55.37 % of java submissions.
*/
class Solution {
    public boolean canReorderDoubled(int[] arr) {
        // count[x] = the number of occurences of x in arr
        Map<Integer, Integer> count = new HashMap<>();
        for (int x: arr)
            count.put(x, count.getOrDefault(x, 0) + 1);
        
        // B = arr as Interger[], sorted by absolute value
        Integer[] B = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++)
            B[i] = arr[i];
        Arrays.sort(B, Comparator.comparingInt(Math::abs));
        
        for (int x: B) {
            // If this can't be consumed, skip
            if (count.get(x) == 0) continue;
            // If this doesn't have a doubled partner, the answer is false
            if (count.getOrDefault(2 * x, 0) <= 0) return false;
            
            // Write x, 2 * x
            count.put(x, count.get(x) - 1);
            count.put(2 * x, count.get(2 * x) - 1);
        }
        
        // If we have written everything, the answer is true
        return true;
    }
}

