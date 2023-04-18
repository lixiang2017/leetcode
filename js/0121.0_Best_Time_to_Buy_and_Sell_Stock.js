/*
执行用时：84 ms, 在所有 JavaScript 提交中击败了58.31% 的用户
内存消耗：50.6 MB, 在所有 JavaScript 提交中击败了75.87% 的用户
通过测试用例：211 / 211
*/
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let ans = 0, prev = prices[0];
    for (let i = 0; i < prices.length; i++) {
        prev = Math.min(prev, prices[i]);
        ans = Math.max(ans, prices[i] - prev);
    }
    return ans;
};