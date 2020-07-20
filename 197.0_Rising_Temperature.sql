# Write your MySQL query statement below
select w1.id from weather w1, weather w2
where w1.temperature > w2.temperature and to_days(w1.recorddate) - to_days(w2.recorddate) = 1

# Success
# Details 
# Runtime: 497 ms, faster than 77.63% of MySQL online submissions for Rising Temperature.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.


# Write your MySQL query statement below
select w1.id from weather w1, weather w2
where w1.temperature > w2.temperature and datediff(w1.recorddate, w2.recorddate) = 1

# Success
# Details 
# Runtime: 763 ms, faster than 37.26% of MySQL online submissions for Rising Temperature.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.


# Write your MySQL query statement below
select w1.id from weather w1, weather w2
where w1.temperature > w2.temperature and subdate(w1.recorddate, 1) = w2.recorddate

# Success
# Details 
# Runtime: 459 ms, faster than 85.23% of MySQL online submissions for Rising Temperature.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.



# Write your MySQL query statement below
# use variables
select id from (
    select 
        case 
            when temperature > @pre_t and datediff(recorddate, @pre_d) = 1 then id 
            else null 
        end as id,
        @pre_t := temperature, @pre_d := recorddate
    from weather, (select @pre_t := null, @pre_d := null) as init order by recorddate asc
) id where id is not null

# Success
# Details 
# Runtime: 392 ms, faster than 91.66% of MySQL online submissions for Rising Temperature.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.

