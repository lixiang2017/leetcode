/*
执行用时：570 ms, 在所有 MySQL 提交中击败了99.47% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
delete from person 
where id in 
(select id from 
    (
        select *,
        row_number() over (partition by email order by id asc) as r
        from person
    ) a where r != 1
)


/*
执行用时：597 ms, 在所有 MySQL 提交中击败了97.65% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
delete from person 
where id not in 
(
    select * from 
    (
        select min(id)
        from person 
        group by email
    ) a
)


/*
执行用时：913 ms, 在所有 MySQL 提交中击败了87.83% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
delete p1 from person p1, person p2
where p1.email = p2.email and p1.id > p2.id
