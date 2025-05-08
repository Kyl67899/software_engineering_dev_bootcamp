--  students table
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    major VARCHAR(100)
)

-- courses table
CREATE TABLE courses(
    id INT PRIMARY KEY,
    title VARCHAR(100),
    department VARCHAR(100)
)

--  enrollment table
CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    grade CHAR(2),
    student_id INT REFERENCES students(id),
    course_id INT REFERENCES courses(id)
)

-- Insert data into students table
INSERT INTO students (id, name, major) VALUES
(1, 'Alice', 'Computer Science'),
(2, 'Bob', 'Mathematics'),
(3, 'Charlie', 'Physics'),
(4, 'David', 'Chemistry'),
(5, 'Eve', 'Biology');

-- Insert data into courses table
INSERT INTO courses (id, title, department) VALUES
(1, 'Data Structures', 'Computer Science'),
(2, 'Calculus', 'Mathematics'),
(3, 'Quantum Mechanics', 'Physics'),
(4, 'Organic Chemistry', 'Chemistry'),
(5, 'Genetics', 'Biology');

-- Insert data into enrollments table
INSERT INTO enrollments (grade, student_id, course_id) VALUES
('A', 1, 1),
('B', 2, 2),
('C', 3, 3),
('A', 4, 4),
('B', 5, 5),
('A', 1, 2);

SELECT * FROM students;

SELECT students.name, courses.title
FROM enrollments
JOIN students ON enrollments.student_id = students.id
JOIN courses ON enrollments.course_id = courses.IDENTIFIED

SELECT students.name, enrollments.grade, courses.title
FROM enrollments
JOIN students ON enrollments.student_id = students.id
JOIN courses ON enrollments.courses_id = courses.id;
