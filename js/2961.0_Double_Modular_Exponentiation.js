/**
 * @param {number[][]} variables
 * @param {number} target
 * @return {number[]}
 */
var getGoodIndices = function(variables, target) {
    const ans = [];
    for (let i = 0; i < variables.length; i++) {
        const v = variables[i];
            if (powMod(powMod(v[0], v[1], 10), v[2], v[3]) == target) {
                ans.push(i);
            }
    }
    return ans;
};

function powMod(x, y, mod) {
    let res = 1;
    while (y > 0) {
        if ((y & 1) == 1) {
            res = res * x % mod;
        }
        x = x * x % mod;
        y >>= 1;
    }
    return res;
}