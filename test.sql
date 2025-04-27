-- Users
-- user_id | name
-- ------------------
-- 101     | Alice
-- 102     | Bob

-- Table 1:
-- Users
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- insert
INSERT INTO name VALUES (101, 'Alice'), (102, 'Bob');

-- fetch 
-- SELECT * FROM users WHERE user_id = 'Alice';

-- Table 2:
-- Jobs
CREATE TABLE jobs (
    job_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    company_name VARCHAR(100) NOT NULL
);

-- insert
INSERT INTO jobs VALUES 
(1, 2001, 'Frontend Dev', 'ABC Corp'), 
(2, 2002, 'Data Analyst', 'XYZ Ltd'), 
(3, 2003, 'Backend Dev', 'DEF Inc');

-- Jobs
-- job_id | title            | company_name
-- -----------------------------------------
-- 2001   | Frontend Dev     | ABC Corp
-- 2002   | Data Analyst     | XYZ Ltd
-- 2003   | Backend Dev      | DEF Inc

-- fetch 
-- SELECT * FROM jobs WHERE title = 'ABC Corp';

-- Table 3:
-- Job application
CREATE TABLE Job_Applications (
    id INT PRIMARY KEY,
    user_id INT, 
    job_id INT,
    application_date DATE, 
    status VARCHAR(50) NOT NULL, 
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (job_id) REFERENCES Users(job_id)
);

-- insert
INSERT INTO Job_Applications VALUES (1, 101, 2001, '2024-04-01 ', 'applied');
INSERT INTO Job_Applications VALUES (2, 102, 2002, '2024-04-03', 'rejected');
INSERT INTO Job_Applications VALUES (3, 101, 2003, '2024-04-05', 'interview');

-- fetch 
-- SELECT * FROM Job_Applications WHERE jobs = 'Sales';

-- Job_Applications
-- id | user_id | job_id | application_date | status
-- ---------------------------------------------------
-- 1  | 101     | 2001   | 2024-04-01       | 'applied'
-- 2  | 102     | 2002   | 2024-04-03       | 'rejected'
-- 3  | 101     | 2003   | 2024-04-05       | 'interview'

-- Task:
-- Write a SQL query that returns the number of job applications submitted by each user, grouped by application status.
-- Expected Output:

-- name   | status     | total_applications
-- ----------------------------------------
-- Alice  | applied    | 1
-- Alice  | interview  | 1
-- Bob    | rejected   | 1

-- 📎 You may include your SQL answer as a .sql file or paste it into your report.

SELECT u.name AS name,
       ja.status,
       COUNT(ja.id) AS total_applications
FROM Job_Applications
JOIN users u ON ja.user_id = u.user_id
GROUP BY u.name, ja.status
