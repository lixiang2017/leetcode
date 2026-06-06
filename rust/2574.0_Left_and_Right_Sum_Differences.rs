impl Solution {
    pub fn left_right_difference(mut nums: Vec<i32>) -> Vec<i32> {
        let total = nums.iter().sum::<i32>();
        let mut left_sum = 0;
        for x in nums.iter_mut() {
            left_sum += *x;
            *x = (left_sum * 2 - *x - total).abs();
        }
        nums
    }
}