/*
approach: Brute Force
Time: O(N^2)
Space: O(1)

执行用时：1117 ms, 在所有 Java 提交中击败了37.43%的用户
内存消耗：41.5 MB, 在所有 Java 提交中击败了27.42%的用户
*/
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;

        for (int end = 0; end < nums.length; end++) {
            int total = 0;
            for (int start = end; start >= 0; start--) {
                total += nums[start];
                if (total == k) {
                    count += 1;
                }
            }
        }

        return count;
    }
}



/*
approach: Prefix Sum + Hash Table (Two Sum)
Time: O(N)
Space: O(N)

执行用时：30 ms, 在所有 Java 提交中击败了50.88%的用户
内存消耗：40.7 MB, 在所有 Java 提交中击败了86.70%的用户
*/
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0, pre = 0;
        HashMap <Integer, Integer> mp = new HashMap <> ();
        mp.put(0, 1);

        for (int i = 0; i < nums.length; i++) {
            pre += nums[i];
            if (mp.containsKey(pre - k)) {
                count += mp.get(pre - k);
            }
            mp.put(pre, mp.getOrDefault(pre, 0) + 1);
        }

        return count;
    }
}


/*
执行用时：25 ms, 在所有 Java 提交中击败了93.98%的用户
内存消耗：40.8 MB, 在所有 Java 提交中击败了78.03%的用户
*/

import java.util.HashMap;

class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0, pre = 0;
        // key: 前缀和
        // value: key 对应的前缀和的个数, the frequency of prefix sum
        HashMap <Integer, Integer> preSumFreq = new HashMap<> ();
        preSumFreq.put(0, 1);
        
        for (int num: nums) {
            pre += num;
            if (preSumFreq.containsKey(pre - k)) {
                count += preSumFreq.get(pre - k);
            }
            preSumFreq.put(pre, preSumFreq.getOrDefault(pre, 0) + 1);
        }

        return count;
    }
}




