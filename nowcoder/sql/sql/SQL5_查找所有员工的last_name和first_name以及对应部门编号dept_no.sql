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



# mysql  #left join
原则是小表驱动大表，
当使用left join时，左表是驱动表，右表是被驱动表，
当使用right join时，右表时驱动表，左表是被驱动表，
当使用inner join时，mysql会选择数据量比较小的表作为驱动表，大表作为被驱动表

select 
    e.last_name,
    e.first_name,
    d.dept_no
from employees as e
left join dept_emp d
on e.emp_no = d.emp_no


# left outer join
select 
    e.last_name,
    e.first_name,
    d.dept_no
from employees as e
left outer join dept_emp d
on e.emp_no = d.emp_no