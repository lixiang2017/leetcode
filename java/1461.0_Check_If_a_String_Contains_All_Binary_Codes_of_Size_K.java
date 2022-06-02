/*
Runtime: 178 ms, faster than 47.92% of Java online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 98 MB, less than 36.46% of Java online submissions for Check If a String Contains All Binary Codes of Size K.
*/

class Solution {
    public boolean hasAllCodes(String s, int k) {
        int need = 1 << k;
        Set<String> got = new HashSet<String>();
        for (int i = k; i <= s.length(); ++i) {
            String a = s.substring(i - k, i);
            if (!got.contains(a)) {
                got.add(a);
                need--;
                if (0 == need) {
                    return true;
                }
            }
        }
        return false;
    }
}



/*
Runtime: 9 ms, faster than 97.92% of Java online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 43.5 MB, less than 96.88% of Java online submissions for Check If a String Contains All Binary Codes of Size K.
*/
class Solution {
    public boolean hasAllCodes(String s, int k) {
        int need = 1 << k;
        boolean[] got = new boolean[need];
        int allOne = need - 1;
        int hashVal = 0;
        for (int i = 0; i < s.length(); ++i) {
            // calculate hash for s.substr(i-k+1, i+1)
            hashVal = ((hashVal << 1) & allOne) | (s.charAt(i) - '0');
            // hash only available when i-k+1 > 0
            if (i >= k - 1 && !got[hashVal]) {
                got[hashVal] = true;
                need--;
                if (0 == need) {
                    return true;
                }
            }
        }
        return false;
    }
}


