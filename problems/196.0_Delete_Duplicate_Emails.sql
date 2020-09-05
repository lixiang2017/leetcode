# Write your MySQL query statement below
delete from person where id not in
(select id from (select MIN(id) id from Person group by email) p)


# Every derived table must have its own alias  # p
# MIN(id) id
# MIN(id) as id


# Success
# Details 
# Runtime: 1670 ms, faster than 90.31% of MySQL online submissions for Delete Duplicate Emails.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.



# Write your MySQL query statement below
delete from person where id not in
(select id from (select MIN(id) as id from Person group by email) p)

# Success
# Details 
# Runtime: 1774 ms, faster than 83.01% of MySQL online submissions for Delete Duplicate Emails.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.



# Write your MySQL query statement below
# ... join ... on ... where ...
delete p2 from person p1 join person p2
on p2.email = p1.email where p2.id > p1.id

# Success
# Details 
# Runtime: 1843 ms, faster than 77.62% of MySQL online submissions for Delete Duplicate Emails.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.



# Write your MySQL query statement below
delete p1 from person p1, person p2
where p1.email = p2.email and p1.id > p2.id

# Success
# Details 
# Runtime: 1798 ms, faster than 81.17% of MySQL online submissions for Delete Duplicate Emails.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.
