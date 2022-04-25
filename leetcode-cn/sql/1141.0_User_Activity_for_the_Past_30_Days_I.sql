/*
执行用时：515 ms, 在所有 MySQL 提交中击败了13.46% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：13 / 13
*/
# Write your MySQL query statement below
select 
    activity_date as day,
    count(distinct user_id) as active_users
from activity
where activity_date between '2019-06-28' and '2019-07-27'
group by activity_date
having active_users > 0

