#week 4 - chapter 15

#--------chapter 15.8 - Many-to-Many Relationships

#many to many relationships
#e.g. one author has written many books but several of his books
#also have many authors (co-authors)

#in order to model these many to many relationships, a table
#inbetween (junction table) is needed which only models these connections.

#the junction table than has a one to many relationship with 
# the left table and a many to one relationship with the right table


#Example of a many-to-many relationship database


"""
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
)
"""

#The table Member is the connector/junction table
#The primary key consists of user_id and course_id
"""
CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
"""

#Insert data into tables User and Course
"""
INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');
"""

#insert data into table Member, create relations
#role = 0: student
#role = 1: instructor

"""
INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);
"""

#Select relations
"""
SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND 
Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name
"""