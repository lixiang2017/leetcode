/*
执行用时：0 ms, 在所有 Rust 提交中击败了100.00% 的用户
内存消耗：2.1 MB, 在所有 Rust 提交中击败了66.67% 的用户
通过测试用例：42 / 42
*/
impl Solution {
    pub fn sum_zero(n: i32) -> Vec<i32> {
        (1 - n..n).step_by(2).collect()
    }
}
