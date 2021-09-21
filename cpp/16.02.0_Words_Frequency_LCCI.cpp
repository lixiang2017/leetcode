/*
执行用时：240 ms, 在所有 C++ 提交中击败了93.42% 的用户
内存消耗：90.7 MB, 在所有 C++ 提交中击败了23.92% 的用户
通过测试用例：24 / 24
*/

class WordsFrequency {
public:
    unordered_map<string, int> umap;
    WordsFrequency(vector<string>& book) {
        for (auto word: book)
            umap[word]++;
    }
    
    int get(string word) {
        // if (!umap.count(word)) return 0;
        return umap[word];
    }
};

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * WordsFrequency* obj = new WordsFrequency(book);
 * int param_1 = obj->get(word);
 */
