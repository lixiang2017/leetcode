/**
执行用时：84 ms, 在所有 JavaScript 提交中击败了37.55% 的用户
内存消耗：39.5 MB, 在所有 JavaScript 提交中击败了5.42% 的用户
通过测试用例：550 / 550
/

/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    const reg = /^([A-Z][a-z]+|[a-z]+|[A-Z]+)$/;
    return reg.test(word);
};




/*
执行用时：80 ms, 在所有 JavaScript 提交中击败了55.96% 的用户
内存消耗：39.5 MB, 在所有 JavaScript 提交中击败了5.06% 的用户
通过测试用例：550 / 550
*/
/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    return /^([A-Z]+|.[a-z]*)$/.test(word);
};


/*
执行用时：72 ms, 在所有 JavaScript 提交中击败了87.00% 的用户
内存消耗：39.3 MB, 在所有 JavaScript 提交中击败了17.33% 的用户
通过测试用例：550 / 550
*/

/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    return /^[A-Z]*$/.test(word) || /^[a-z]*$/.test(word) || /^[A-Z][a-z]*$/.test(word);
};
