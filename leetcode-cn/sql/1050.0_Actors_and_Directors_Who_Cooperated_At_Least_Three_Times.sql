'''
执行用时：364 ms, 在所有 MySQL 提交中击败了75.28% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select 
    actor_id, director_id
from actordirector
group by actor_id, director_id
having count(1) >= 3


'''
执行用时：1079 ms, 在所有 MySQL 提交中击败了5.09% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select 
    actor_id, director_id
from actordirector
group by 1, 2
having count(1) >= 3
