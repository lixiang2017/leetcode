/*
执行用时：4 ms, 在所有 Go 提交中击败了27.47% 的用户
内存消耗：2.6 MB, 在所有 Go 提交中击败了96.14% 的用户
通过测试用例：256 / 256
*/
func simplifyPath(path string) string {
    return filepath.Clean(path)
}
