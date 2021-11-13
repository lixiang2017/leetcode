/*
执行用时：0 ms, 在所有 Rust 提交中击败了100.00% 的用户
内存消耗：1.9 MB, 在所有 Rust 提交中击败了100.00% 的用户
通过测试用例：550 / 550
*/

impl Solution {
    pub fn detect_capital_use(word: String) -> bool {
        word[1..].chars().all(|c| c.is_ascii_lowercase()) || word.chars().all(|c| c.is_ascii_uppercase())
    }
}