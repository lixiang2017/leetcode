/**
 * @param {number[]} nums
 * @return {number}
 */
var minElement = function(nums) {
    let ans = Infinity;
    for (let x of nums) {
        let s = 0;
        while (x > 0) {
            s += x % 10;
            x = Math.floor(x / 10);
        }
        ans = Math.min(ans, s);
    }
    return ans;
};


/**
 * @param {number[]} nums
 * @return {number}
 */
var minElement = function(nums) {
    let ans = Infinity;
    for (let x of nums) {
        let s = 0;
        while (x > 0) {
            s += x % 10;
            if (s > ans) break;
            x = Math.floor(x / 10);
        }
        ans = Math.min(ans, s);
    }
    return ans;
};