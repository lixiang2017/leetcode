/*
执行用时：218 ms, 在所有 MySQL 提交中击败了47.65% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select * from cinema
where id % 2 = 1 and description != 'boring'
order by rating desc;


/*
执行用时：208 ms, 在所有 MySQL 提交中击败了81.73% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select * from cinema
where id % 2 and description <> 'boring'
order by rating desc;


/*
执行用时：224 ms, 在所有 MySQL 提交中击败了36.23% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select * from cinema
where id & 1 and description <> 'boring'
order by rating desc;


/*
执行用时：212 ms, 在所有 MySQL 提交中击败了68.44% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select id, movie, description, rating 
from cinema
where id & 1 and description <> 'boring'
order by 4 desc;


/*
执行用时：230 ms, 在所有 MySQL 提交中击败了27.39% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select id, movie, description, rating 
from cinema
where mod(id, 2) and description <> 'boring'
order by 4 desc;



/*
having

执行用时：210 ms, 在所有 MySQL 提交中击败了75.85% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select id, movie, description, rating 
from cinema
having mod(id, 2) and description <> 'boring'
order by 4 desc;
















