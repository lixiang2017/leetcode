'''
执行用时：477 ms, 在所有 MySQL 提交中击败了84.25% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select player_id,
min(event_date) as first_login
from activity 
group by player_id 


'''
执行用时：495 ms, 在所有 MySQL 提交中击败了56.10% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select player_id, event_date as first_login
from (
    select 
    player_id,
    event_date,
    rank() over (partition by player_id order by event_date) as rk 
    from activity 
    # group by player_id
) t where rk = 1



'''
执行用时：490 ms, 在所有 MySQL 提交中击败了63.97% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select player_id, event_date as first_login
from (
    select 
    player_id,
    event_date,
    row_number() over (partition by player_id order by event_date) as rn 
    from activity 
) t where rn = 1


'''
执行用时：507 ms, 在所有 MySQL 提交中击败了42.96% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select 
    distinct player_id, 
    min(event_date) over (partition by player_id order by event_date) as first_login
from activity 


'''
执行用时：501 ms, 在所有 MySQL 提交中击败了48.77% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select 
    distinct player_id, 
    first_value(event_date) over (partition by player_id order by event_date) as first_login
from activity 







