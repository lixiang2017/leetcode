/*
执行用时：48 ms, 在所有 Go 提交中击败了95.83% 的用户
内存消耗：7.3 MB, 在所有 Go 提交中击败了79.17% 的用户
通过测试用例：51 / 51
*/
func gardenNoAdj(n int, paths [][]int) []int {
    g := make([][]int, n)
    for _, e := range paths {
        x, y := e[0] - 1, e[1] - 1
        g[x] = append(g[x], y)
        g[y] = append(g[y], x)
    }
    color := make([]int, n)
    for i, nodes := range g {
        mask := uint8(1)
        for _, j := range nodes {
            mask |= 1 << color[j]
        }
        color[i] = bits.TrailingZeros8(^mask)
    }
    return color
}
