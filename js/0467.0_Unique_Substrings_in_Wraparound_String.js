/*
执行用时：72 ms, 在所有 JavaScript 提交中击败了64.81% 的用户
内存消耗：43 MB, 在所有 JavaScript 提交中击败了48.15% 的用户
通过测试用例：81 / 81
*/

/**
 * @param {string} p
 * @return {number}
 */
var findSubstringInWraproundString = function(p) {
    const dp = new Array(26).fill(0);
    let k = 0;
    for (let i = 0; i < p.length; ++i) {
        if (i > 0 && (p[i].charCodeAt() - p[i - 1].charCodeAt() + 26) % 26 == 1) {
            ++k;
        } else {
            k = 1;
        }
        dp[p[i].charCodeAt() - 'a'.charCodeAt()] = Math.max(dp[p[i].charCodeAt() - 'a'.charCodeAt()], k);
    }

    return _.sum(dp);
};
