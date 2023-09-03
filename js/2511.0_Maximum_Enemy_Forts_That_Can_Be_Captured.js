/*
60ms, 击败 66.67%使用 JavaScript 的用户
39.81MB, 击败 94.87%使用 JavaScript 的用户
*/
/**
 * @param {number[]} forts
 * @return {number}
 */
var captureForts = function(forts) {
    let ans = 0, pre = -1;
    for (let i = 0; i < forts.length; i++) {
        if (forts[i] != 0) {
            if (pre >= 0 && forts[i] != forts[pre]) {
                ans = Math.max(ans, i - pre - 1);
            }
            pre = i;
        }
    }
    return ans;
};


/*
var, not let
64ms, 击败 41.03%使用 JavaScript 的用户
40.02MB, 击败 76.92%使用 JavaScript 的用户
*/
/**
 * @param {number[]} forts
 * @return {number}
 */
var captureForts = function(forts) {
    var ans = 0, pre = -1;
    for (var i = 0; i < forts.length; i++) {
        if (forts[i] != 0) {
            if (pre >= 0 && forts[i] != forts[pre]) {
                ans = Math.max(ans, i - pre - 1);
            }
            pre = i;
        }
    }
    return ans;
};
