-- 行转列

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



-- (id, month) is the primary key of this table.
-- 使用group bY 后，如果你直接查询某个字段比如 id， revenue 默认都是取得第一个，
-- 所以这个地方要加上一个 max 获取分组后的最大值
-- 用任何一个聚合函数都可，配合group by 使用
-- 单独地使用group by (不加聚合函数)，只能显示出每组记录的第一条记录。
-- 今后但凡使用group by，前面一定要有聚合函数（MAX /MIN / SUM /AVG / COUNT）
/*
笔记:
    列转行 行转列 一般都需要聚合函数 否则取到第一个符合条件的就结束了
    case when的用法使得第一次满足就结束
    一般也要加上group by 先独立分组再聚合
    小细节: sum后要直接跟括号 不能有空格 其他函数应该也如此
*/


# 执行用时：456 ms, 在所有 MySQL 提交中击败了85.25% 的用户
# 内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# 通过测试用例：16 / 16
# Write your MySQL query statement below
select id,
sum(case `month` when 'Jan' then revenue else null  end) as 'Jan_Revenue',
sum(case `month` when 'Feb' then revenue else null  end) as 'Feb_Revenue',
sum(case `month` when 'Mar' then revenue else null  end) as 'Mar_Revenue',
sum(case `month` when 'Apr' then revenue else null  end) as 'Apr_Revenue',
sum(case `month` when 'May' then revenue else null  end) as 'May_Revenue',
sum(case `month` when 'Jun' then revenue else null  end) as 'Jun_Revenue',
sum(case `month` when 'Jul' then revenue else null  end) as 'Jul_Revenue',
sum(case `month` when 'Aug' then revenue else null  end) as 'Aug_Revenue',
sum(case `month` when 'Sep' then revenue else null  end) as 'Sep_Revenue',
sum(case `month` when 'Oct' then revenue else null  end) as 'Oct_Revenue',
sum(case `month` when 'Nov' then revenue else null  end) as 'Nov_Revenue',
sum(case `month` when 'Dec' then revenue else null  end) as 'Dec_Revenue'
from department
group by id


# 执行用时：457 ms, 在所有 MySQL 提交中击败了84.73% 的用户
# 内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# 通过测试用例：16 / 16
# Write your MySQL query statement below
select distinct id,
sum(IF(month="Jan",revenue,null)) as Jan_Revenue,
sum(IF(month="Feb",revenue,null)) as Feb_Revenue,
sum(IF(month="Mar",revenue,null)) as Mar_Revenue,
sum(IF(month="Apr",revenue,null)) as Apr_Revenue,
sum(IF(month="May",revenue,null)) as May_Revenue,
sum(IF(month="Jun",revenue,null)) as Jun_Revenue,
sum(IF(month="Jul",revenue,null)) as Jul_Revenue,
sum(IF(month="Aug",revenue,null)) as Aug_Revenue,
sum(IF(month="Sep",revenue,null)) as Sep_Revenue,
sum(IF(month="Oct",revenue,null)) as Oct_Revenue,
sum(IF(month="Nov",revenue,null)) as Nov_Revenue,
sum(IF(month="Dec",revenue,null)) as Dec_Revenue
from Department 
group by id order by id;





# 执行用时：453 ms, 在所有 MySQL 提交中击败了86.34% 的用户
# 内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# 通过测试用例：16 / 16
# Write your MySQL query statement below
SELECT 
    id, 
    max(if(month = 'Jan',revenue,null)) Jan_Revenue,
    max(if(month = 'Feb',revenue,null)) Feb_Revenue,
    max(if(month = 'Mar',revenue,null)) Mar_Revenue,
    max(if(month = 'Apr',revenue,null)) Apr_Revenue,
    max(if(month = 'May',revenue,null)) May_Revenue,
    max(if(month = 'Jun',revenue,null)) Jun_Revenue,
    max(if(month = 'Jul',revenue,null)) Jul_Revenue,
    max(if(month = 'Aug',revenue,null)) Aug_Revenue,
    max(if(month = 'Sep',revenue,null)) Sep_Revenue,
    max(if(month = 'Oct',revenue,null)) Oct_Revenue,
    max(if(month = 'Nov',revenue,null)) Nov_Revenue,
    max(if(month = 'Dec',revenue,null)) Dec_Revenue
FROM Department GROUP BY id



-- 执行用时：1767 ms, 在所有 mssql 提交中击败了61.82% 的用户
-- 内存消耗：0 B, 在所有 mssql 提交中击败了100.00% 的用户
-- 通过测试用例：16 / 16
/* Write your T-SQL query statement below */
select a.id,
a.Jan Jan_Revenue,
a.Feb Feb_Revenue,
a.Mar Mar_Revenue,
a.Apr Apr_Revenue,
a.May May_Revenue,
a.Jun Jun_Revenue,
a.Jul Jul_Revenue,
a.Aug Aug_Revenue,
a.Sep Sep_Revenue,
a.Oct Oct_Revenue,
a.Nov Nov_Revenue,
a.Dec Dec_Revenue 
from Department 
pivot (
    max(revenue) 
    for month in(Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec)
) a




/*
执行用时：1319 ms, 在所有 oraclesql 提交中击败了24.42% 的用户
内存消耗：0 B, 在所有 oraclesql 提交中击败了100.00% 的用户
通过测试用例：16 / 16
*/
/* Write your PL/SQL query statement below */
SELECT *
FROM department
PIVOT (SUM(revenue) as "Revenue" 
for month in (
'Jan' as "Jan",
'Feb' as "Feb",
'Mar' as "Mar",
'Apr' as "Apr",
'May' as "May",
'Jun' as "Jun",
'Jul' as "Jul",
'Aug' as "Aug",
'Sep' as "Sep",
'Oct' as "Oct",
'Nov' as "Nov",
'Dec' as "Dec"
));


/*
执行用时：506 ms, 在所有 MySQL 提交中击败了29.84% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：16 / 16
*/
# Write your MySQL query statement below
select distinct 
    d.id,
    d1.revenue Jan_Revenue,
    d2.revenue Feb_Revenue,
    d3.revenue Mar_Revenue,
    d4.revenue Apr_Revenue,
    d5.revenue May_Revenue,
    d6.revenue Jun_Revenue,
    d7.revenue Jul_Revenue,
    d8.revenue Aug_Revenue,
    d9.revenue Sep_Revenue,
    d10.revenue Oct_Revenue,
    d11.revenue Nov_Revenue,
    d12.revenue Dec_Revenue
from department d
left join department d1 on d.id = d1.id and d1.month = "Jan"
left join department d2 on d.id = d2.id and d2.month = "Feb"
left join department d3 on d.id = d3.id and d3.month = "Mar"
left join department d4 on d.id = d4.id and d4.month = "Apr"
left join department d5 on d.id = d5.id and d5.month = "May"
left join department d6 on d.id = d6.id and d6.month = "Jun"
left join department d7 on d.id = d7.id and d7.month = "Jul"
left join department d8 on d.id = d8.id and d8.month = "Aug"
left join department d9 on d.id = d9.id and d9.month = "Sep"
left join department d10 on d.id = d10.id and d10.month = "Oct"
left join department d11 on d.id = d11.id and d11.month = "Nov"
left join department d12 on d.id = d12.id and d12.month = "Dec"













