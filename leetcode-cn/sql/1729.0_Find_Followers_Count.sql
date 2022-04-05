/*
执行用时：610 ms, 在所有 MySQL 提交中击败了19.93% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select 
    user_id,
    count(1) as followers_count
from followers
group by user_id
order by user_id


# Write your MySQL query statement below
select 
    user_id,
    count(2) as followers_count
from followers
group by user_id
order by user_id


# Write your MySQL query statement below
select 
    user_id,
    count(3) as followers_count
from followers
group by user_id
order by user_id


# Write your MySQL query statement below
select 
    user_id,
    count(0) as followers_count
from followers
group by user_id
order by user_id


