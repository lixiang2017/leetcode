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



/*
with
https://dev.mysql.com/doc/refman/8.0/en/with.html

执行用时：601 ms, 在所有 MySQL 提交中击败了56.42% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
with unbanned_user as (select * from users where banned = 'No')

select  
total_table.request_at as 'Day', 
round(ifnull(cancel_cnt / total, 0), 2) as 'Cancellation Rate'
from 
(
    select 
    count(*) as cancel_cnt, 
    request_at    -- as 'Cancellation Rate'
    from trips 
    where client_id in (select users_id from unbanned_user)
    and driver_id in (select users_id from unbanned_user)
    and request_at between "2013-10-01" and "2013-10-03"
    and status in ('cancelled_by_client', 'cancelled_by_driver')
    group by request_at
)  cancel_table
right join 
(
    select 
    count(*) as total, 
    request_at    -- as 'Cancellation Rate'
    from trips 
    where client_id in (select users_id from unbanned_user)
    and driver_id in (select users_id from unbanned_user)
    and request_at between "2013-10-01" and "2013-10-03"
    group by request_at
)  total_table
on cancel_table.request_at = total_table.request_at



/*
执行用时：596 ms, 在所有 MySQL 提交中击败了62.14% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
with unbanned_user as (select * from users where banned = 'No')

select 
request_at as `Day`, 
round( count(if(status in ('cancelled_by_client', 'cancelled_by_driver'), status, null))  / count(1), 2) as `Cancellation Rate`
from trips 
where client_id in (select users_id from unbanned_user)
and driver_id in (select users_id from unbanned_user)
and request_at between "2013-10-01" and "2013-10-03"
group by request_at

/*
join on
执行用时：669 ms, 在所有 MySQL 提交中击败了16.56% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
with unbanned_user as (select users_id from users where banned = 'No')

select 
request_at as `Day`, 
round( count(if(status in ('cancelled_by_client', 'cancelled_by_driver'), status, null))  / count(1), 2) as `Cancellation Rate`
from trips 
join unbanned_user un1 on client_id = un1.users_id
join unbanned_user un2 on driver_id = un2.users_id
where request_at between "2013-10-01" and "2013-10-03"
group by request_at


/*
count(if(status like 'cancelled%', status, null))

执行用时：671 ms, 在所有 MySQL 提交中击败了15.79% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
with unbanned_user as (select users_id from users where banned = 'No')

select 
request_at as `Day`, 
round( count(if(status like 'cancelled%', status, null))  / count(1), 2) as `Cancellation Rate`
from trips 
inner join unbanned_user un1 on client_id = un1.users_id
inner join unbanned_user un2 on driver_id = un2.users_id
where request_at >= "2013-10-01" and request_at <= "2013-10-03"
group by request_at


/*
 sum(status like 'cancelled%')

执行用时：641 ms, 在所有 MySQL 提交中击败了27.93% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
with unbanned_user as (select users_id from users where banned = 'No')

select 
request_at as `Day`, 
round( sum(status like 'cancelled%') / count(1), 2) as `Cancellation Rate`
from trips 
inner join unbanned_user un1 on client_id = un1.users_id
inner join unbanned_user un2 on driver_id = un2.users_id
where request_at >= "2013-10-01" and request_at <= "2013-10-03"
group by request_at


/*
sum(case when status like 'cancelled%' then 1 else 0 end)

执行用时：659 ms, 在所有 MySQL 提交中击败了20.32% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
*/
# Write your MySQL query statement below
with unbanned_user as (select users_id from users where banned = 'No')

select 
request_at as `Day`, 
round( sum(case when status like 'cancelled%' then 1 else 0 end) / count(1), 2) as `Cancellation Rate`
from trips 
inner join unbanned_user un1 on client_id = un1.users_id
inner join unbanned_user un2 on driver_id = un2.users_id
where request_at >= "2013-10-01" and request_at <= "2013-10-03"
group by request_at




