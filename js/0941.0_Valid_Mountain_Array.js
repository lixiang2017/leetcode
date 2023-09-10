/*
76ms 击败 22.22%使用 JavaScript 的用户
42.34MB 击败 64.05%使用 JavaScript 的用户
*/
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function(arr) {
    const n = arr.length;
    let i = 0, j = n - 1;
    while (i < j && arr[i] < arr[i + 1]) {
        i++;
    }
    while (i < j && arr[j] < arr[j - 1]) {
        j--;
    }
    return i == j && i > 0 && j < n - 1;
};
