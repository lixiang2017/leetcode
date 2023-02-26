/*
执行用时：64 ms, 在所有 JavaScript 提交中击败了36.84% 的用户
内存消耗：40.9 MB, 在所有 JavaScript 提交中击败了100.00% 的用户
通过测试用例：70 / 70
*/
/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumSwap = function(s1, s2) {
    let xy = 0, yx = 0;
    const n = s1.length;
    for (let i = 0; i < n; i++) {
        const a = s1[i], b = s2[i];
        if (a === 'x' && b === 'y') {
            xy++;
        }
        else if (a === 'y' && b === 'x') {
            yx++;
        }
    }
    if (((xy + yx) & 1) == 1) {
        return -1;
    }
    return Math.floor(xy / 2) + Math.floor(yx/ 2) + xy % 2 + yx % 2;
};
