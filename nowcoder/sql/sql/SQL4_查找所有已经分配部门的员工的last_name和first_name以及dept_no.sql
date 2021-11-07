drop table if exists  `dept_emp` ; 
drop table if exists  `employees` ; 
CREATE TABLE `dept_emp` (
`emp_no` int(11) NOT NULL,
`dept_no` char(4) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));
CREATE TABLE `employees` (
`emp_no` int(11) NOT NULL,
`birth_date` date NOT NULL,
`first_name` varchar(14) NOT NULL,
`last_name` varchar(16) NOT NULL,
`gender` char(1) NOT NULL,
`hire_date` date NOT NULL,
PRIMARY KEY (`emp_no`));
INSERT INTO dept_emp VALUES(10001,'d001','1986-06-26','9999-01-01');
INSERT INTO dept_emp VALUES(10002,'d002','1996-08-03','9999-01-01');
INSERT INTO employees VALUES(10001,'1953-09-02','Georgi','Facello','M','1986-06-26');
INSERT INTO employees VALUES(10002,'1964-06-02','Bezalel','Simmel','F','1985-11-21');
INSERT INTO employees VALUES(10003,'1959-12-03','Parto','Bamford','M','1986-08-28');
INSERT INTO employees VALUES(10004,'1954-05-01','Chirstian','Koblick','M','1986-12-01');



# mysql  # join
SELECT
    e.last_name,
    e.first_name,
    d.dept_no
from employees e
JOIN dept_emp d
on e.emp_no = d.emp_no


# inner join
SELECT
    e.last_name,
    e.first_name,
    d.dept_no
from employees e
inner JOIN dept_emp d
on e.emp_no = d.emp_no

# left join
SELECT
    e.last_name,
    e.first_name,
    d.dept_no
from employees e
left JOIN dept_emp d
on e.emp_no = d.emp_no
where d.dept_no is not NULL


# right join
SELECT
    e.last_name,
    e.first_name,
    d.dept_no
from employees e
right JOIN dept_emp d
on e.emp_no = d.emp_no 
where d.dept_no is not NULL

# right join
SELECT
    e.last_name,
    e.first_name,
    d.dept_no
from employees e
right JOIN dept_emp d
on e.emp_no = d.emp_no 


# where
SELECT
    e.last_name,
    e.first_name,
    d.dept_no
from employees e, dept_emp d
where e.emp_no = d.emp_no 


# natural join #  只有一列是公有的，用自然连接呀
SELECT
    e.last_name,
    e.first_name,
    d.dept_no
from employees e
NATURAL join dept_emp d
