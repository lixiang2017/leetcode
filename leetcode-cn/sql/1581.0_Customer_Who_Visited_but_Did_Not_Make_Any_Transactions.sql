/*
执行用时：1366 ms, 在所有 MySQL 提交中击败了56.11% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：28 / 28
*/
# Write your MySQL query statement below
/*
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 4        | 30          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+
*/

select customer_id, count(*) as count_no_trans
from visits v where visit_id not in (select visit_id from transactions)
group by customer_id 
order by count_no_trans desc 
