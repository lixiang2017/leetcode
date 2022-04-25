/*
执行用时：543 ms, 在所有 MySQL 提交中击败了76.07% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select 
    date_id, 
    make_name, 
    count(distinct lead_id) unique_leads, 
    count(distinct partner_id) unique_partners
from dailysales
group by date_id, make_name


/*
执行用时：537 ms, 在所有 MySQL 提交中击败了83.71% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select 
    date_id, 
    make_name, 
    count(distinct lead_id) unique_leads, 
    count(distinct partner_id) unique_partners
from dailysales
group by 1, 2


/*
执行用时：562 ms, 在所有 MySQL 提交中击败了55.82% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select a.date_id, a.make_name, unique_leads, unique_partners
from (
    select date_id, make_name,
    count(distinct lead_id) as unique_leads
    from dailysales
    group by date_id, make_name
) a join (
    select date_id, make_name,
    count(distinct partner_id) as unique_partners
    from dailysales
    group by date_id, make_name
) b on a.date_id = b.date_id and a.make_name = b.make_name





