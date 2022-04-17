/*
63 / 63 个通过测试用例
状态：通过
执行用时: 248 ms
内存消耗: 18.4 MB
提交时间：18 小时前

a - x - y - b
*/

func maximumScore(scores []int, edges [][]int) int {
    type nb struct{ to, s int }
    g := make([][]nb, len(scores))
    for _, e := range edges {
        x, y := e[0], e[1]
        g[x] = append(g[x], nb{y, scores[y]})
        g[y] = append(g[y], nb{x, scores[x]})
    }
    for i, vs := range g {
        sort.Slice(vs, func(i, j int) bool { return vs[i].s > vs[j].s })
        if len(vs) > 3 {
            vs = vs[: 3]
        }
        g[i] = vs 
    }

    ans := -1
    for _, e := range edges {
        x, y := e[0], e[1]
        for _, a := range g[x] {
            for _, b := range g[y] {
                if a.to != y && b.to != x && a.to != b.to {
                    ans = max(ans, a.s + scores[x] + scores[y] + b.s)
                }
            }
        }
    }
    return ans
}

func max(a, b int) int {
    if b > a {
        return b
    };
    return a
}
