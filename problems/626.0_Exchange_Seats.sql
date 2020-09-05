# Write your MySQL query statement below
select s.id, s.student
from (
    select id - 1 as id, student
    from seat 
    where id % 2 = 0
    union
        select 
            (case when (cnt % 2 = 1) and id = cnt then id else id + 1 end) as id,
            student
        from 
            seat,
            (select count(*) as cnt from seat) as seatcnt
        where id % 2 = 1
) s
order by s.id asc

# Success
# Details 
# Runtime: 370 ms, faster than 59.70% of MySQL online submissions for Exchange Seats.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Exchange Seats.


# Write your MySQL query statement below
# more simple
select s.id, s.student
from (
    select id - 1 as id, student
    from seat 
    where id % 2 = 0
    union
        select 
            (case when id = cnt then id else id + 1 end) as id,
            student
        from 
            seat,
            (select count(*) as cnt from seat) as seatcnt
        where id % 2 = 1
) s
order by s.id

# Success
# Details 
# Runtime: 311 ms, faster than 74.68% of MySQL online submissions for Exchange Seats.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Exchange Seats.



# Write your MySQL query statement below
select * from
(
    select id + 1 as id, student from seat where id % 2 = 1 and id not in (select max(id) from seat)
    union
    select id - 1, student from seat where id % 2 = 0
    union
    select id, student from seat where id % 2 <> 0 and id in (select max(id) from seat)
) as s
order by id

# Success
# Details 
# Runtime: 266 ms, faster than 92.80% of MySQL online submissions for Exchange Seats.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Exchange Seats.


# Write your MySQL query statement below
select 
(
    case
        when ((select max(id) from seat) % 2 = 1 and id = (select max(id) from seat)) then id
        when id % 2 = 1 then id + 1
        else id - 1
    end
) as id, student

from seat 
order by id

# Success
# Details 
# Runtime: 265 ms, faster than 93.03% of MySQL online submissions for Exchange Seats.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Exchange Seats.



# Write your MySQL query statement below
select 
(
    case
        when mod(id, 2) <> 0 and id != (select count(*) from seat) then id + 1
        when mod(id, 2) = 0 then id -1
        else id   # max odd
    end
) as id, student
from seat 
order by 1

# Success
# Details 
# Runtime: 258 ms, faster than 95.32% of MySQL online submissions for Exchange Seats.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Exchange Seats.

















