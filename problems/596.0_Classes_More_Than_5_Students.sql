# Write your MySQL query statement below
select class  from courses group by class having count(distinct student) >= 5

# Success
# Details 
# Runtime: 304 ms, faster than 82.75% of MySQL online submissions for Classes More Than 5 Students.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Classes More Than 5 Students.


# Note: The students should not be counted duplicate in each course. # use distinct
# test case
{'headers': {'courses': ['student', 'class']},
 'rows': {'courses': [['A', 'Math'],
                      ['B', 'English'],
                      ['C', 'Math'],
                      ['D', 'Biology'],
                      ['E', 'Math'],
                      ['F', 'Math'],
                      ['A', 'Math']]}}

output: {"headers": ["class"], "values": [["Math"]]}


# Write your MySQL query statement below
select class from (
    select distinct student, class from courses
) tmp
group by class
having count(student) > 4
# Every derived table must have its own alias  # use tmp alisas for the derived table

# Success
# Details 
# Runtime: 285 ms, faster than 90.84% of MySQL online submissions for Classes More Than 5 Students.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Classes More Than 5 Students.



# Write your MySQL query statement below
select x.class  from (
    select count(distinct c.student) as numStudents, c.class
    from courses c
    group by class
) x
where x.numStudents > 4

# Success
# Details 
# Runtime: 512 ms, faster than 36.77% of MySQL online submissions for Classes More Than 5 Students.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Classes More Than 5 Students.
