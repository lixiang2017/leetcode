/*
流式处理

执行用时：76 ms, 在所有 Java 提交中击败了6.45%的用户
内存消耗：41.6 MB, 在所有 Java 提交中击败了61.48%的用户
通过测试用例：185 / 185
*/
class Solution {
    public int numUniqueEmails(String[] emails) {
        return (int) Arrays.stream(emails).map(email -> { 
            email = email.replaceAll("\\+.*@", "@"); 
            while (email.matches(".*\\..*@.*")) { 
                email = email.replaceFirst("\\.", ""); 
            } return email; 
        }).distinct().count();
    } 
}



/*
执行用时：27 ms, 在所有 Java 提交中击败了14.04% 的用户
内存消耗：42.1 MB, 在所有 Java 提交中击败了24.66% 的用户
通过测试用例：185 / 185
*/
class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> unique = new HashSet<>();
        for (String email: emails) {
            String[] parts = email.split("@");
            parts[0] = parts[0].split("\\+")[0];
            parts[0] = parts[0].replaceAll("\\.", "");
            unique.add(parts[0] + "@" + parts[1]);
        }
        return unique.size();
    }
}
