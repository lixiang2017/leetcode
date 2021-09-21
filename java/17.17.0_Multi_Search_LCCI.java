/*
Trie

执行用时：46 ms, 在所有 Java 提交中击败了85.24% 的用户
内存消耗：61.7 MB, 在所有 Java 提交中击败了28.18% 的用户
通过测试用例：32 / 32
*/

class Solution {
    class TrieNode {
        String end;
        TrieNode[] next = new TrieNode[26];
    }

    class Trie {
        TrieNode root;
        public Trie(String[] words) {
            root = new TrieNode();
            for (String word: words) {
                TrieNode node = root;
                for (char ch: word.toCharArray()) {
                    int i = ch - 'a';
                    if (node.next[i] == null) {
                        node.next[i] = new TrieNode();
                    }
                    node = node.next[i];
                }
                node.end = word;
            }
        }

        public List<String> search(String str) {
            TrieNode node = root;
            List<String> res = new ArrayList<>();
            for (char c: str.toCharArray()) {
                int i = c - 'a';
                if (node.next[i] == null) {
                    break;
                }
                node = node.next[i];
                if (node.end != null) {
                    res.add(node.end);
                }
            }
            return res;
        }
    }

    public int[][] multiSearch(String big, String[] smalls) {
        Trie trie = new Trie(smalls);
        Map<String, List<Integer>> hit = new HashMap<>();
        for (int i = 0; i < big.length(); i++) {
            List<String> matches = trie.search(big.substring(i));
            for (String word: matches) {
                if (!hit.containsKey(word)) {
                    hit.put(word, new ArrayList<>());
                }
                hit.get(word).add(i);
            }
        }

        int[][] res = new int[smalls.length][];
        for (int i = 0; i < smalls.length; i++) {
            List<Integer> list = hit.get(smalls[i]);
            if (list == null) {
                res[i] = new int[0];
                continue;
            }
            int size = list.size();
            res[i] = new int[size];
            for (int j = 0; j < size; ++j) {
                res[i][j] = list.get(j);
            }
        }
        return res;
    }
}
