/*
执行用时：468 ms, 在所有 Go 提交中击败了5.26% 的用户
内存消耗：76.4 MB, 在所有 Go 提交中击败了5.26% 的用户
*/

func nthSuperUglyNumber(n int, primes []int) (ugly int) {
    seen := map[int] bool{1: true}
    h := &hp{[]int{1}}
    for i := 0; i < n; i++ {
        ugly = heap.Pop(h).(int)
        for _, prime := range primes {
            if next := ugly * prime; !seen[next] {
                seen[next] = true
                heap.Push(h, next)
            }
        }
    }
    return
}

type hp struct{ sort.IntSlice}
func (h *hp) Push(v interface{}) {
    h.IntSlice = append(h.IntSlice, v.(int))
}
func (h *hp) Pop() interface{} {
    a := h.IntSlice;
    v := a[len(a) - 1];
    h.IntSlice = a[:len(a) - 1];
    return v
}
