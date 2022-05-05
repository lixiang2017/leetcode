/*
执行用时：56 ms, 在所有 JavaScript 提交中击败了99.61% 的用户
内存消耗：47 MB, 在所有 JavaScript 提交中击败了82.19% 的用户
通过测试用例：29 / 29
*/

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let arr = s.split(' ');
    for (let i = 0; i < arr.length; i++) {
        let num = arr[i].split('').reverse().join('');
        arr[i] = num;
    }
    return arr.join(' ');
};


/*
执行用时：72 ms, 在所有 JavaScript 提交中击败了73.81% 的用户
内存消耗：47.1 MB, 在所有 JavaScript 提交中击败了70.57% 的用户
通过测试用例：29 / 29
*/
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    return s.split(' ').map(item => item.split('').reverse().join('')).join(' ')
};
