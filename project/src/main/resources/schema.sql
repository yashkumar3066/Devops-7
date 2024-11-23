-- Table to store user details from Keycloak
CREATE TABLE users (
                       user_id VARCHAR(36) PRIMARY KEY,       -- Keycloak's unique user identifier (sub claim)
                       username VARCHAR(50) NOT NULL,         -- Keycloak's preferred_username
                       email VARCHAR(100) NOT NULL,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store information about courses
CREATE TABLE courses (
                         course_id VARCHAR(36) PRIMARY KEY,     -- UUID as VARCHAR
                         title VARCHAR(100) NOT NULL,           -- Course title
                         details TEXT,                          -- Description or details of the course
                         semester VARCHAR(20),                  -- Semester in which the course is offered
                         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Join table to store enrollments (many-to-many relationship between users and courses)
CREATE TABLE user_courses (
                              user_course_id VARCHAR(36) PRIMARY KEY, -- UUID as VARCHAR
                              user_id VARCHAR(36) NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
                              course_id VARCHAR(36) NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
                              enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                              is_enrolled BOOLEAN DEFAULT true         -- Indicates if the user is currently enrolled in the course
);

INSERT INTO users (user_id, username, email, created_at)
VALUES
    ('f1e87db2-eca0-469d-b5f2-d2f3d5c03720', 'user1', 'user1@example.com', CURRENT_TIMESTAMP),
    ('a3d8d8f0-0109-468b-b13f-65f6d3c3e77a', 'user2', 'user2@example.com', CURRENT_TIMESTAMP),
    ('b4e87d5c-eca0-469d-b5f2-d2f3d5c03721', 'user3', 'user3@example.com', CURRENT_TIMESTAMP);
INSERT INTO courses (course_id, title, details, semester, created_at)
VALUES
    ('123e4567-e89b-12d3-a456-426614174001', 'Introduction to Java', 'Learn the basics of Java programming language', 'Fall 2024', CURRENT_TIMESTAMP),
    ('987e6543-9abc-11d3-a456-426614174002', 'Data Structures', 'Learn about various data structures like arrays, linked lists, and trees', 'Fall 2024', CURRENT_TIMESTAMP),
    ('abcd1234-efgh-56ij-7890-klmn12345678', 'Database Systems', 'Learn the fundamentals of database design and SQL', 'Spring 2025', CURRENT_TIMESTAMP);
INSERT INTO user_courses (user_course_id, user_id, course_id, enrolled_at, is_enrolled)
VALUES
    ('1', 'f1e87db2-eca0-469d-b5f2-d2f3d5c03720', '123e4567-e89b-12d3-a456-426614174001', CURRENT_TIMESTAMP, true),
    ('2', 'f1e87db2-eca0-469d-b5f2-d2f3d5c03720', '987e6543-9abc-11d3-a456-426614174002', CURRENT_TIMESTAMP, true),
    ('3', 'a3d8d8f0-0109-468b-b13f-65f6d3c3e77a', 'abcd1234-efgh-56ij-7890-klmn12345678', CURRENT_TIMESTAMP, true),
    ('4', 'b4e87d5c-eca0-469d-b5f2-d2f3d5c03721', '123e4567-e89b-12d3-a456-426614174001', CURRENT_TIMESTAMP, true),
    ('5', 'b4e87d5c-eca0-469d-b5f2-d2f3d5c03721', '987e6543-9abc-11d3-a456-426614174002', CURRENT_TIMESTAMP, false);  -- user3 is not enrolled in this course
