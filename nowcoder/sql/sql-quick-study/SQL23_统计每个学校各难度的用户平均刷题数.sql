drop table if exists `user_profile`;
drop table if  exists `question_practice_detail`;
CREATE TABLE `user_profile` (
`id` int NOT NULL,
`device_id` int NOT NULL,
`gender` varchar(14) NOT NULL,
`age` int ,
`university` varchar(32) NOT NULL,
`gpa` float,
`active_days_within_30` int ,
`question_cnt` int ,
`answer_cnt` int 
);
CREATE TABLE `question_practice_detail` (
`id` int NOT NULL,
`device_id` int NOT NULL,
`question_id`int NOT NULL,
`result` varchar(32) NOT NULL
);
CREATE TABLE `question_detail` (
`id` int NOT NULL,
`question_id`int NOT NULL,
`difficult_level` varchar(32) NOT NULL
);

INSERT INTO user_profile VALUES(1,2138,'male',21,'北京大学',3.4,7,2,12);
INSERT INTO user_profile VALUES(2,3214,'male',null,'复旦大学',4.0,15,5,25);
INSERT INTO user_profile VALUES(3,6543,'female',20,'北京大学',3.2,12,3,30);
INSERT INTO user_profile VALUES(4,2315,'female',23,'浙江大学',3.6,5,1,2);
INSERT INTO user_profile VALUES(5,5432,'male',25,'山东大学',3.8,20,15,70);
INSERT INTO user_profile VALUES(6,2131,'male',28,'山东大学',3.3,15,7,13);
INSERT INTO user_profile VALUES(7,4321,'male',28,'复旦大学',3.6,9,6,52);
INSERT INTO question_practice_detail VALUES(1,2138,111,'wrong');
INSERT INTO question_practice_detail VALUES(2,3214,112,'wrong');
INSERT INTO question_practice_detail VALUES(3,3214,113,'wrong');
INSERT INTO question_practice_detail VALUES(4,6543,111,'right');
INSERT INTO question_practice_detail VALUES(5,2315,115,'right');
INSERT INTO question_practice_detail VALUES(6,2315,116,'right');
INSERT INTO question_practice_detail VALUES(7,2315,117,'wrong');
INSERT INTO question_practice_detail VALUES(8,5432,117,'wrong');
INSERT INTO question_practice_detail VALUES(9,5432,112,'wrong');
INSERT INTO question_practice_detail VALUES(10,2131,113,'right');
INSERT INTO question_practice_detail VALUES(11,5432,113,'wrong');
INSERT INTO question_practice_detail VALUES(12,2315,115,'right');
INSERT INTO question_practice_detail VALUES(13,2315,116,'right');
INSERT INTO question_practice_detail VALUES(14,2315,117,'wrong');
INSERT INTO question_practice_detail VALUES(15,5432,117,'wrong');
INSERT INTO question_practice_detail VALUES(16,5432,112,'wrong');
INSERT INTO question_practice_detail VALUES(17,2131,113,'right');
INSERT INTO question_practice_detail VALUES(18,5432,113,'wrong');
INSERT INTO question_practice_detail VALUES(19,2315,117,'wrong');
INSERT INTO question_practice_detail VALUES(20,5432,117,'wrong');
INSERT INTO question_practice_detail VALUES(21,5432,112,'wrong');
INSERT INTO question_practice_detail VALUES(22,2131,113,'right');
INSERT INTO question_practice_detail VALUES(23,5432,113,'wrong');
INSERT INTO question_detail VALUES(1,111,'hard');
INSERT INTO question_detail VALUES(2,112,'medium');
INSERT INTO question_detail VALUES(3,113,'easy');
INSERT INTO question_detail VALUES(4,115,'easy');
INSERT INTO question_detail VALUES(5,116,'medium');
INSERT INTO question_detail VALUES(6,117,'easy');




# mysql  # inner join
select up.university,
qd.difficult_level,
count(qpb.question_id) / count(distinct qpb.device_id) as avg_answer_cnt
from question_practice_detail qpb
inner join user_profile up on qpb.device_id = up.device_id
inner join question_detail qd on qpb.question_id = qd.question_id
group by up.university, qd.difficult_level


# join 
select up.university,
qd.difficult_level,
count(qpb.question_id) / count(distinct qpb.device_id) as avg_answer_cnt
from question_practice_detail qpb
join user_profile up on qpb.device_id = up.device_id
join question_detail qd on qpb.question_id = qd.question_id
group by up.university, qd.difficult_level


# left join
select up.university,
qd.difficult_level,
count(qpb.question_id) / count(distinct qpb.device_id) as avg_answer_cnt
from question_practice_detail qpb
left join user_profile up on qpb.device_id = up.device_id
left join question_detail qd on qpb.question_id = qd.question_id
group by up.university, qd.difficult_level



# 表的顺序其实也没有关系
select up.university,
qd.difficult_level,
count(qpb.question_id) / count(distinct qpb.device_id) as avg_answer_cnt
from user_profile up 
join question_practice_detail qpb on qpb.device_id = up.device_id
join question_detail qd on qpb.question_id = qd.question_id
group by up.university, qd.difficult_level


# where
select up.university,
qd.difficult_level,
count(qpb.question_id) / count(distinct qpb.device_id) as avg_answer_cnt
from user_profile up,
question_detail qd,
question_practice_detail qpb
where qpb.question_id = qd.question_id and qpb.device_id = up.device_id
group by up.university, qd.difficult_level
