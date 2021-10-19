/*
执行用时：582 ms, 在所有 MySQL 提交中击败了38.63% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/


# Write your MySQL query statement below
select 
request_at as `Day`,
(
    round(count(if(status != 'completed', status, null)) / count(status), 2)
) as `Cancellation Rate`
from 
(
    select a.*
    from 
    (
        select * from trips where "2013-10-01" <= request_at and request_at <= "2013-10-03"
    ) a 
    inner join users u1 on a.client_id = u1.users_id
    inner join users u2 on a.driver_id = u2.users_id
    where u1.banned != 'Yes' and u2.banned != 'Yes'
) f1
group by request_at
