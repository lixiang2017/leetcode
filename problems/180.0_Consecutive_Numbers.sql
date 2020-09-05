# Write your MySQL query statement below
select distinct l1.num as consecutivenums
from logs l1, logs l2, logs l3
where l1.id = l2.id - 1 and l2.id = l3.id -1 and l1.num = l2.num and l2.num = l3.num

# Success
# Details 
# Runtime: 456 ms, faster than 91.32% of MySQL online submissions for Consecutive Numbers.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Consecutive Numbers.


# Write your MySQL query statement below
select distinct l1.num as consecutivenums
from logs l1
join logs l2 on l1.id = l2.id - 1
join logs l3 on l1.id = l3.id - 2
where l1.num = l2.num and l2.num = l3.num

# Success
# Details 
# Runtime: 574 ms, faster than 60.90% of MySQL online submissions for Consecutive Numbers.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Consecutive Numbers.



# Write your MySQL query statement below
select distinct num as consecutivenums from
(
    select num, @count := if(@pre = num, @count + 1, 1) as n, @pre := num
    from logs, (select @count := 0, @pre := -1) as init
) as t where t.n >= 3


# Success
# Details 
# Runtime: 426 ms, faster than 97.20% of MySQL online submissions for Consecutive Numbers.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Consecutive Numbers.
