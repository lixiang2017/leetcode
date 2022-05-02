/*
stack
T: O(M + N)
S: O(M + N)

Runtime: 6 ms, faster than 13.13% of Java online submissions for Backspace String Compare.
Memory Usage: 42.6 MB, less than 23.96% of Java online submissions for Backspace String Compare.
*/
class Solution {
    public boolean backspaceCompare(String s, String t) {
        return build(s).equals(build(t));
    }
    
    public String build(String s) {
        Stack<Character> ans = new Stack();
        for (char c: s.toCharArray()) {
            if (c != '#')
                ans.push(c);
            else if (!ans.empty())
                ans.pop();
        }
        return String.valueOf(ans);
    }
}


/*
two pointers
T: O(M + N)
S: O(1)


Runtime: 1 ms, faster than 87.48% of Java online submissions for Backspace String Compare.
Memory Usage: 42.4 MB, less than 38.67% of Java online submissions for Backspace String Compare.
*/
class Solution {
    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1, j = t.length() - 1;
        int skips = 0, skipt = 0;
        
        // while there may be chars in build(s) or build(t)
        while (i >= 0 || j >= 0) {
            // find position of next possible char in build(s)
            while (i >= 0) {
                if (s.charAt(i) == '#') {skips++; i--;}
                else if (skips > 0) {skips--; i--;}
                else break;
            }
            // find position of next possible char in build(t)
            while (j >= 0) {
                if (t.charAt(j) == '#') {skipt++; j--;}
                else if (skipt > 0) {skipt--; j--;}
                else break;
            }
            // if two actual characters are different
            if (i >= 0 && j >= 0 && s.charAt(i) != t.charAt(j)) {
                return false;
            }
            // if expecting to compare char vs nothing
            if ((i >= 0) != (j >= 0))
                return false;
            i--; j--;
        }
        return true;    
    }
}





