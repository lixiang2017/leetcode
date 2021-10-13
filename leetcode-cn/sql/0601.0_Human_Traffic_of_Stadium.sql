/*
执行用时：380 ms, 在所有 MySQL 提交中击败了26.57% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select distinct a.* from stadium a, stadium b, stadium c
where a.people >= 100 and b.people >= 100 and c.people >= 100 and
(
    (a.id = b.id - 1 and b.id = c.id - 1) or 
    (b.id = a.id - 1 and a.id = c.id - 1) or
    (b.id = c.id - 1 and c.id = a.id - 1)
)
order by id



/*
执行用时：413 ms, 在所有 MySQL 提交中击败了11.85% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select id, visit_date, people from
(
    select *,
        lead(people, 1) over(order by visit_date) as next1,
        lead(people, 2) over(order by visit_date) as next2,
        lag(people, 1) over(order by visit_date) as pre1,
        lag(people, 2) over(order by visit_date) as pre2
    from stadium
) t
where people >= 100 and (
    pre1 >= 100 and pre2 >= 100 or
    pre1 >= 100 and next1 >= 100 or
    next1 >= 100 and next2 >= 100
)
