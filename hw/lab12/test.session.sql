-- Create a table named books with the following structure:
-- • id – SERIAL PRIMARY KEY
-- • title – VARCHAR(100) NOT NULL
-- • author – VARCHAR(100) NOT NULL
-- • year_published – INT
CREATE TABLE genre(
	id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    year_published INT NOT NULL
);

-- Insert the following records into the books table:
-- title author year_published
-- The Great Gatsby F. Scott Fitzgerald 1925

-- Animal Farm George Orwell 1945
-- To Kill a Mockingbird Harper Lee 1960
-- Brave New World Aldous Huxley 1932

INSERT INTO genre (title, author, year_published) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
('Animal Farm', 'George Orwell', 1945),
('To Kill a Mockingbird', 'Harper Lee', 1960),
('Brave New World', 'Aldous Huxley', 1932);

-- Select all records from the books table
SELECT * FROM genre;

-- Update the data Update the year_published of Brave New World to 1931
UPDATE genre 
SET year_published = 1931
WHERE title = 'Brave New World';

-- Delete the record for To Kill a Mockingbird.
DELETE FROM genre
WHERE title = 'To Kill a Mockingbird';

-- Select all records from the books table to verify your changes
SELECT * FROM genre;

-- Add a new column genre to the books table
-- Update the genre for each book
-- Select all books grouped by genre

ALTER TABLE genre
ADD genre VARCHAR(100);

UPDATE genre 
SET genre= 'Fiction'
WHERE title IN ('THE GREAT GATSBY', 'TO KILL A MOCKINGBIRD');

