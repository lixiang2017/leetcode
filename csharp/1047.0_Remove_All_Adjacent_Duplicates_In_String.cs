/*
stack
T: O(N)
S: O(N)

Runtime: 133 ms, faster than 83.41% of C# online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 38.3 MB, less than 78.20% of C# online submissions for Remove All Adjacent Duplicates In String.
*/
public class Solution {
    public string RemoveDuplicates(string s) {
        StringBuilder sb = new StringBuilder(s[0]);
        for (int i = 0; i < s.Length; ++i) {
            if (sb.Length > 0 && s[i] == sb[sb.Length - 1]) {
                sb.Remove(sb.Length - 1, 1);
            } else {
                sb.Append(s[i]);
            }
        }
        return sb.ToString();
    }
}


/*
stack
T: O(N)
S: O(N)

Runtime: 129 ms, faster than 85.31% of C# online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 38 MB, less than 92.42% of C# online submissions for Remove All Adjacent Duplicates In String.
*/
public class Solution {
    public string RemoveDuplicates(string s) {
        StringBuilder sb = new StringBuilder();
        foreach (char c in s) {
            if (sb.Length > 0 && c == sb[sb.Length - 1]) {
                sb.Length--;
            } else {
                sb.Append(c);
            }
        }
        return sb.ToString();
    }
}


/*
char array

Runtime: 98 ms, faster than 92.42% of C# online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 39 MB, less than 65.88% of C# online submissions for Remove All Adjacent Duplicates In String.
*/
public class Solution {
    public string RemoveDuplicates(string s) {
        char[] output = new char[s.Length];
        int position = -1;
        foreach (char c in s) {
            if (position >= 0 && c == output[position]) {
                position--;
            } else {
                output[++position] = c;
            }
        }
        return new string(output.Take(position + 1).ToArray());
    }
}
