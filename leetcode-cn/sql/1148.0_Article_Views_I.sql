/*
执行用时：436 ms, 在所有 MySQL 提交中击败了42.33% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：13 / 13
*/
# Write your MySQL query statement below
select 
distinct(author_id) as id
from views
where author_id = viewer_id
order by id 



/*
执行用时：421 ms, 在所有 MySQL 提交中击败了68.39% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：13 / 13
*/
# Write your MySQL query statement below
select author_id as id from 
(
    select distinct * from views
    where author_id = viewer_id 
) a 
group by author_id
order by id


/*
执行用时：435 ms, 在所有 MySQL 提交中击败了46.89% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：13 / 13
*/
# Write your MySQL query statement below
select distinct author_id as id from views
where author_id = viewer_id 
order by id
