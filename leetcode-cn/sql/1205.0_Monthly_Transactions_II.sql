
#执行用时：362 ms, 在所有 MySQL 提交中击败了100.00% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户

ref:
https://leetcode-cn.com/problems/monthly-transactions-ii/solution/xin-shou-kan-cong-ti-yi-li-jie-dao-mysql-ji-chu-zh/

# Write your MySQL query statement below
SELECT month, country,
COUNT(IF(tag = 1, 1, NULL)) AS approved_count,
SUM(IF(tag = 1, amount, 0)) AS approved_amount,
COUNT(IF(tag = 0, 1, NULL)) AS chargeback_count,
SUM(IF(tag = 0, amount, 0)) AS chargeback_amount
FROM (
    SELECT country, amount, 1 as tag,
    date_format(trans_date, "%Y-%m") AS month
    FROM Transactions
    WHERE state = 'approved'

    UNION ALL

    SELECT country, amount, 0 as tag,
    date_format(c.trans_date, "%Y-%m") AS month
    FROM Transactions AS t RIGHT OUTER JOIN Chargebacks AS c
    ON t.id = c.trans_id
) AS T
GROUP BY month, country

# COUNT(IF(tag = 1, 1, 0)) AS approved_count # will be wrong
