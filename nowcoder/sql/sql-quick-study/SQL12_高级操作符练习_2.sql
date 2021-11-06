drop table if exists user_profile;
CREATE TABLE `user_profile` (
`id` int NOT NULL,
`device_id` int NOT NULL,
`gender` varchar(14) NOT NULL,
`age` int ,
`university` varchar(32) NOT NULL,
`province` varchar(32)  NOT NULL,
`gpa` float);
INSERT INTO user_profile VALUES(1,2138,'male',21,'北京大学','BeiJing',3.4);
INSERT INTO user_profile VALUES(2,3214,'male',null,'复旦大学','Shanghai',4.0);
INSERT INTO user_profile VALUES(3,6543,'female',20,'北京大学','BeiJing',3.2);
INSERT INTO user_profile VALUES(4,2315,'female',23,'浙江大学','ZheJiang',3.6);
INSERT INTO user_profile VALUES(5,5432,'male',25,'山东大学','Shandong',3.8);


# mysql
select device_id, gender, age, university, gpa from user_profile
where university = '北京大学' or gpa > 3.7
