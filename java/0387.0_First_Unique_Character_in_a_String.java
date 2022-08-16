/*
hash table
T: O(2N)
S: O(26)

Runtime: 38 ms, faster than 52.76% of Java online submissions for First Unique Character in a String.
Memory Usage: 54.1 MB, less than 32.38% of Java online submissions for First Unique Character in a String.
*/
class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> count = new HashMap<Character, Integer>();
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        for (int i = 0; i < n; ++i) {
            if (count.get(s.charAt(i)) == 1)
                return i;
        }
        return -1;
    }
}



/*
Runtime: 11 ms, faster than 80.68% of Java online submissions for First Unique Character in a String.
Memory Usage: 49 MB, less than 57.98% of Java online submissions for First Unique Character in a String.
*/
class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        int n = s.length();
        for (int i = 0; i < n; i++) {
            int index = s.charAt(i) - 'a';
            count[index]++;
        }
        for (int i = 0; i < n; ++i) {
            int index = s.charAt(i) - 'a';
            if (count[index] == 1)
                return i;
        }
        return -1;
    }
}
