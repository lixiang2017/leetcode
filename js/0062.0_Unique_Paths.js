/*
Runtime: 43 ms, faster than 96.39% of JavaScript online submissions for Unique Paths.
Memory Usage: 42 MB, less than 60.21% of JavaScript online submissions for Unique Paths.
*/
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const path = Array(m).fill(0).map(() => Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        path[i][0] = 1;
    }
    for (let j = 0; j < n; j++) {
        path[0][j] = 1;
    }
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            path[i][j] = path[i - 1][j] + path[i][j - 1];
        }
    }
    return path[m - 1][n - 1];
};
