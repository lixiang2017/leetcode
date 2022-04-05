/* Write your PL/SQL query statement below */
select
    user_id,
    initcap(name) name
from users
order by user_id


/*
执行用时：626 ms, 在所有 MySQL 提交中击败了58.22% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：21 / 21
*/
# Write your MySQL query statement below
select
    user_id,
    concat(upper(left(name, 1)), lower(substring(name, 2))) as name 
from users
order by user_id


/*
执行用时：627 ms, 在所有 MySQL 提交中击败了56.54% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：21 / 21
*/
# Write your MySQL query statement below
select
    user_id,
    concat(upper(substring(name, 1, 1)), lower(substring(name, 2))) as name 
from users
order by user_id


/*
执行用时：614 ms, 在所有 MySQL 提交中击败了73.31% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：21 / 21
*/
# Write your MySQL query statement below
select
    user_id,
    concat(upper(left(name, 1)), lower(right(name, length(name) - 1))) as name 
from users
order by user_id



# Write your MySQL query statement below
select
    user_id,
    concat(upper(first_part), lower(second_part)) as name 
from 
(
    select *, 
    substring(name from 1 for 1) as first_part,
    substring(name from 2 for 1000000) as second_part 
    from users
) a 
order by user_id



