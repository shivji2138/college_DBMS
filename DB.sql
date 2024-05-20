CREATE DATABASE collage;
USE collage;
CREATE TABLE Students (
student_id INT PRIMARY KEY,
stu_name VARCHAR(100),
date_of_birth DATE,
phone_number VARCHAR(15),
address VARCHAR(255),
email VARCHAR(100),
department varchar(40),
acadamic_year INT
);
CREATE TABLE COURSES (
COURSE_ID int PRIMARY KEY, 
COURSE_NAME varchar(55),
COURSE_FEES int,
DURATION_YR int
);
CREATE TABLE Fees_STATUS (
STUDENT_ID int PRIMARY KEY, 
STU_NAME varchar(50),
COURSE_ID int,
TOTAL_FEES int, 
PAID_FEES int,
BALANCE_FEES int,
foreign key (course_id) references coures(course_id)
);
CREATE TABLE Attendence (
STUDENT_ID int, 
SEM_1 varchar(10), 
SEM_2 varchar(10),
SEM_3 varchar(10),
SEM_4 varchar(10),
SEM_5 varchar(10),
SEM_6 varchar(10),
SEM_7 varchar(10),
SEM_8 varchar(10), 
COURSE_ID int,
foreign key (STUDENT_ID) references STUDENTS(STUDENT_ID)
);
CREATE TABLE STUDENTS_MARKS (
Exam_Roll int primary key,
student_id int,
SEM_1 int,
SEM_2 INT,
SEM_3 int,
SEM_4 int,
SEM_5 int,
SEM_6 int,
SEM_7 int,
SEM_8 int
)