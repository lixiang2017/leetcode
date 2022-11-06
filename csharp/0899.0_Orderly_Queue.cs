/*
Runtime: 148 ms, faster than 14.29% of C# online submissions for Orderly Queue.
Memory Usage: 39.1 MB, less than 14.29% of C# online submissions for Orderly Queue.
*/
public class Solution {
    public string OrderlyQueue(string s, int k) {
        if (k > 1) {
            return string.Concat(s.OrderBy(x => x));
        }
        string ans = s;
        foreach (char c in s) {
            s = s[1..] + s[0];
            if (s.CompareTo(ans) < 0) ans = s;
        }
        return ans;
    }
}


/*
Runtime: 150 ms, faster than 14.29% of C# online submissions for Orderly Queue.
Memory Usage: 39 MB, less than 14.29% of C# online submissions for Orderly Queue.
*/
public class Solution {
    public string OrderlyQueue(string s, int k) => k > 1 ?
        string.Concat(s.OrderBy(x => x)) :
        s.Min(c => s = $"{s[1..]}{c}");
}


/*
Runtime: 162 ms, faster than 14.29% of C# online submissions for Orderly Queue.
Memory Usage: 38.6 MB, less than 14.29% of C# online submissions for Orderly Queue.
*/
public class Solution {
    public string OrderlyQueue(string s, int k) {
        if (1 == k) {
            string ans = s;
            for (int i = 1; i < s.Length; ++i) {
                string m = s[i..] + s[..i];
                if (m.CompareTo(ans) < 0) ans = m;
            }
            return ans;
        }
        char[] characters = s.ToCharArray();
        Array.Sort(characters);
        return new string(characters);
    }
}

/*
Runtime: 140 ms, faster than 28.57% of C# online submissions for Orderly Queue.
Memory Usage: 38.7 MB, less than 14.29% of C# online submissions for Orderly Queue.
*/
public class Solution {
    public string OrderlyQueue(string s, int k) {
        if (1 == k) {
            string sTwice = s + s;
            for (int i = 1; i < s.Length; ++i) {
                string m = sTwice.Substring(i, s.Length);
                if (m.CompareTo(s) < 0) s = m;
            }
            return s;
        }
        char[] characters = s.ToCharArray();
        Array.Sort(characters);
        return new string(characters);        
    }
}



/*
Runtime: 163 ms, faster than 14.29% of C# online submissions for Orderly Queue.
Memory Usage: 39.1 MB, less than 14.29% of C# online submissions for Orderly Queue.
*/
public class Solution {
    public string OrderlyQueue(string s, int k) 
        => k > 1
            ? string.Join("", s.OrderBy(x => x))
            : Enumerable.Range(0, s.Length).Select(i => s[i..] + s[..i]).Min()!;
}
