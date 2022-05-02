'''
执行用时：823 ms, 在所有 MySQL 提交中击败了68.80% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：17 / 17
'''
# Write your MySQL query statement below
select 
    u.name,
    if(r.distance is null, 0, sum(r.distance)) as travelled_distance
from users u 
left join rides r 
on u.id = r.user_id
group by user_id
order by travelled_distance desc, name asc


'''
执行用时：824 ms, 在所有 MySQL 提交中击败了67.73% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：17 / 17
'''
# Write your MySQL query statement below
select 
    u.name,
    ifnull(sum(r.distance), 0) as travelled_distance
from users u 
left join rides r 
on u.id = r.user_id
group by user_id
order by travelled_distance desc, name asc

