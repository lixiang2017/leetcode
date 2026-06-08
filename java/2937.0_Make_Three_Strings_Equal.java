class Solution {
    public int findMinimumOperations(String s1, String s2, String s3) {
        int n = Math.min(Math.min(s1.length(), s2.length()), s3.length());
        int i = 0;
        while (i < n && s2.charAt(i) == s1.charAt(i) && s3.charAt(i) == s1.charAt(i)) {
            i++;
        }
        return i == 0 ? -1 : s1.length() + s2.length() + s3.length() - i * 3;
    }
}