/*
执行用时：368 ms, 在所有 JavaScript 提交中击败了87.50% 的用户
内存消耗：69.4 MB, 在所有 JavaScript 提交中击败了56.82% 的用户
通过测试用例：24 / 24
*/

/**
 * @param {string[]} book
 */
var WordsFrequency = function(book) {
    this.map = {}
    for (let item of book) {
        if (!this.map[item]) {
            this.map[item] = 1
        } else {
            this.map[item]++
        }
    }
};

/** 
 * @param {string} word
 * @return {number}
 */
WordsFrequency.prototype.get = function(word) {
    return this.map[word] ? this.map[word] : 0
};

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * var obj = new WordsFrequency(book)
 * var param_1 = obj.get(word)
 */
 