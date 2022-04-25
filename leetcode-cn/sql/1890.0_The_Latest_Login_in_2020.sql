'''
执行用时：648 ms, 在所有 MySQL 提交中击败了44.60% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：23 / 23
'''
# Write your MySQL query statement below
select 
    user_id,
    max(time_stamp) as last_stamp
from (
    select *
    from logins
    where DATE_FORMAT(time_stamp, '%Y') = '2020'
) t 
group by user_id


'''
执行用时：720 ms, 在所有 MySQL 提交中击败了16.67% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：23 / 23
'''
# Write your MySQL query statement below
select 
    user_id,
    max(time_stamp) as last_stamp
from logins
where DATE_FORMAT(time_stamp, '%Y') = '2020'
group by user_id


'''
执行用时：795 ms, 在所有 MySQL 提交中击败了7.20% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：23 / 23
'''
# Write your MySQL query statement below
select 
    user_id,
    max(time_stamp) as last_stamp
from logins
where time_stamp between '2020-01-01 00:00:00' and '2021-01-01 00:00:00'
group by user_id


'''
执行用时：640 ms, 在所有 MySQL 提交中击败了51.54% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：23 / 23
'''
# Write your MySQL query statement below
select 
    user_id,
    max(time_stamp) as last_stamp
from logins
where left(time_stamp, 4) = '2020'
group by user_id


'''
执行用时：648 ms, 在所有 MySQL 提交中击败了44.60% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：23 / 23
'''
# Write your MySQL query statement below
select 
    user_id,
    max(time_stamp) as last_stamp
from logins
where year(time_stamp) = '2020'
group by user_id


'''
执行用时：644 ms, 在所有 MySQL 提交中击败了47.64% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：23 / 23
'''
# Write your MySQL query statement below
select 
    user_id,
    max(time_stamp) as last_stamp
from logins
where extract(year from time_stamp) = 2020
#  where time_stamp between '2020-01-01 00:00:00' and '2021-01-01 00:00:00'
group by user_id


