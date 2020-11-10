#week 2 - chapter 15 - SQL Structured Query Language

#------15.1 - Relational Databases
#store data in a database for analyzing

#relational databases: 
#This model organizes data into one or more tables (or "relations") 
# of columns and rows, with a unique key identifying each row. 
# Rows are also called records or tuples. Columns are also called 
# attributes. Generally, each table/relation represents one "entity type" 
# (such as customer or product). The rows represent instances of that 
# type of entity (such as "Lee" or "chair") and the columns representing 
# values attributed to that instance (such as address or price). 

#query - Abfrage

#database - contains many tables
#relation (or table) - contains tuples and attributes
#tuple (or row) - a set of fields that represents an "object"
#                 e.g. "person" or "music track"
#attribute - one of possibly many elements of data corresponding
#            to the object represented by the row


#------15.2 - Using Databases
#big application often consist of an Application Software and a
#Database Data Server
#A Developer who writes the Application Software
#A Database Administrator (DBA) builds Database Tools for the 
#Database Data Server to run as efficient as possible

#a database model or database schema is the 
#structure or format of a database

#Compared to other SQL databases, SQLite is so small, that is build
# #into applications such as music players, python, a lot of smartphone
# #apps etc.


#------15.3 - Single Table CRUD

#creates a table named "Users" with two columns "name" and "email"
"""
#both with 128 characters as a limit
CREATE TABLE Users(
	name VARCHAR(128),
	email VARCHAR(128)
)
"""

#insert a row  with data
"""
INSERT INTO Users (name,email) VALUES ("Kristin","kf@umich.edu")
"""

#delete rows
"""
#deletes a row in a table based on a selection criteria
DELETE FROM Users WHERE email="ted@umich.edu"
"""

#update rows
"""
#update of a field with a where clause
UPDATE Users SET name="Charles" WHERE email="csev@umich.edu"
"""

#select columns and/or rows
"""
#select all columns "*" and rows from USERS
#select all rows because there is no WHERE clause after Users
SELECT * FROM Users

#select all columns from Users where the email equals ...
SELECT * FROM Users WHERE email="csev@umich.edu"
"""

#order data by
"""
SELECT * FROM Users ORDER BY email

SELECT * FROM Users ORDER BY name
"""