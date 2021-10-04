/*
执行用时：108 ms, 在所有 JavaScript 提交中击败了100.00% 的用户
内存消耗：50.6 MB, 在所有 JavaScript 提交中击败了100.00% 的用户
通过测试用例：93 / 93
*/

/**
 * @param {number[]} stones
 * @return {boolean}
 */
var stoneGameIX = function(stones) {
    let c = new Array(3).fill(0)
    for (let x of stones) c[x % 3]++
    if (c[0] % 2) return Math.abs(c[1] - c[2]) >= 3
    return c[1] > 0 && c[2] > 0
};
