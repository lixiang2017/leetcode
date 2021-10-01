/*
执行用时：293 ms, 在所有 MySQL 提交中击败了80.05% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
## max odd
select id, student
from seat where id & 1 and id in (select max(id) from seat)
union
## common odd
select (id + 1) as id, student
from seat where id & 1 and id not in (select max(id) from seat)
union
## even
select (id - 1) as id, student
from seat where id & 1 = 0
order by id;



/*
执行用时：314 ms, 在所有 MySQL 提交中击败了42.32% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
select 
(case
    when mod(id, 2) and id = (select max(id) from seat) then id
    when mod(id, 2) then id + 1
    else id - 1
end) as id,
student
from seat 
order by id;



/*
执行用时：317 ms, 在所有 MySQL 提交中击败了38.43% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
# 利用异或只把偶数减2，奇数不变，从而调位。
# 异或 （两个数异或，二级制 最后一位不一样才为 1） ，如果id是奇数 id - 1 最后一位变 0， 异或后 大小不变，偶数 id id - 1 ，异或后 值 减小2
select rank() over(order by (id-1)^1) as id, student from seat


/*
执行用时：299 ms, 在所有 MySQL 提交中击败了68.47% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
select row_number() over () as id, student
from seat
order by if (id % 2, id, id - 2)



/*
执行用时：294 ms, 在所有 MySQL 提交中击败了78.43% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
select 
    row_number() over (order by if(mod(id, 2), id + 1, id - 1)) as id, 
    student
from seat


/*
执行用时：302 ms, 在所有 MySQL 提交中击败了62.61% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
select 
    rank() over (order by if(mod(id, 2), id + 1, id - 1)) as id, 
    student
from seat









