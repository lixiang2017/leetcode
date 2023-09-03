/*
132ms 击败 97.50%使用 JavaScript 的用户
52.09MB 击败 87.50%使用 JavaScript 的用户
*/


/**
 * @param {number[]} dist
 * @param {number[]} speed
 * @return {number}
 */
var eliminateMaximum = function(dist, speed) {
    const n = dist.length;
    const arrivalTimes = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        arrivalTimes[i] = Math.ceil(dist[i] / speed[i]);
    }
    arrivalTimes.sort((a, b) => (a - b));
    for (let i = 0; i < n; i++) {
        if (arrivalTimes[i] <= i) {
            return i;
        }
    }
    return n;
};