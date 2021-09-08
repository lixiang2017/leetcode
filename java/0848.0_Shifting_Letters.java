/*
Runtime: 18 ms, faster than 24.91% of Java online submissions for Shifting Letters.
Memory Usage: 98.4 MB, less than 5.58% of Java online submissions for Shifting Letters.
*/
class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        StringBuilder ans = new StringBuilder();
        int x = 0;
        for (int shift: shifts)
            x = (x + shift) % 26;
        
        for (int i = 0; i < s.length(); ++i) {
            int index = s.charAt(i) - 'a';
            ans.append((char) ((index + x) % 26 + 97) );
            x = Math.floorMod(x - shifts[i], 26);
        }
        return ans.toString();
    }
}
