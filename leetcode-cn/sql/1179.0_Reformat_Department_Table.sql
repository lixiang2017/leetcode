# 执行用时：460 ms, 在所有 MySQL 提交中击败了81.83% 的用户
# 内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# 通过测试用例：16 / 16

# Write your MySQL query statement below
select id,
sum(case when month = "Jan" then revenue else null end) Jan_Revenue,
sum(case when month = "Feb" then revenue else null end) Feb_Revenue,
sum(case when month = "Mar" then revenue else null end) Mar_Revenue,
sum(case when month = "Apr" then revenue else null end) Apr_Revenue,
sum(case when month = "May" then revenue else null end) May_Revenue,
sum(case when month = "Jun" then revenue else null end) Jun_Revenue,
sum(case when month = "Jul" then revenue else null end) Jul_Revenue,
sum(case when month = "Aug" then revenue else null end) Aug_Revenue,
sum(case when month = "Sep" then revenue else null end) Sep_Revenue,
sum(case when month = "Oct" then revenue else null end) Oct_Revenue,
sum(case when month = "Nov" then revenue else null end) Nov_Revenue,
sum(case when month = "Dec" then revenue else null end) Dec_Revenue
from department
group by id
