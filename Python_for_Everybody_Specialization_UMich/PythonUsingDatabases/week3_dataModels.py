#week 3 - chapter 15 - Data Models and Relational SQL

#------15.4 - Designing a Data Model
#when you want to analyze a lot of data speed gets important

#putting all the data into one table of a database makes the database slow
#therefore to increase speed you need to build a specific data model

#basic rule: do not put the same string data in twice
#-> use a relationship instead
#e.g. music database with genres, many tracks are of the same genre
#e.g. "metal", instead of assigning tracks of the same genre the 
#string "metal" it is better to assign a number to the genre "metal" 
# and to the respective metal tracks

#when building a data model, which table should you build first?
#-> the most important
#e.g. for a "track" database the track table is the most important
#for a album database the album table is the most important

#a data model creates the features of an application


#------15.5 - Representing a Data Model in Tables
#primary key - a unique number to refer to a row

#connecting two tables by pointing from a foreign key of table 1
#to a primary key of table 2

#logical key - a key which is easy to understand for the user
#e.g. "title" and which can be used in a WHERE clause

#id: primary key (which cannot be null/zero and is numbered uniquely
# automatically)
#artist_id: foreign key
#title: logical key
"""
CREATE TABLE Album(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id   INTEGER,
    title   TEXT
)
"""

"""
CREATE TABLE Artist(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT
)
"""

"""
CREATE TABLE Genre (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT
)
"""

"""
CREATE TABLE Track (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT, 
	album_id  INTEGER,
	genre_id  INTEGER,
	len INTEGER, rating INTEGER, count INTEGER
)
"""

#------15.6 - Inserting Relational Data
#inserting data in our database
"""
insert into Artist (name) values ('Led Zepplin')
insert into Artist (name) values ('AC/DC')
insert into Genre (name) values ('Rock')
insert into Genre (name) values ('Metal')
"""

#the artist_id comes from the "id" of the Artist table which was
#auto assigned -> this is a relationship!
"""
insert into Album (title, artist_id) values ('Who Made Who', 2)
insert into Album (title, artist_id) values ('IV', 1)
"""

#by executing these we get replicated album id's, which is good
#replicated integers are fast but replicated strings are slow
"""
insert into Track (title, rating, len, count, album_id, genre_id) 
     values ('Black Dog', 5, 297, 0, 2, 1)
insert into Track (title, rating, len, count, album_id, genre_id)
     values ('Stairway', 5, 482, 0, 2, 1)
insert into Track (title, rating, len, count, album_id, genre_id) 
     values ('About to Rock', 5, 313, 0, 1, 2)
insert into Track (title, rating, len, count, album_id, genre_id) 
     values ('Who Made Who', 5, 207, 0, 1, 2)
"""


#------15.7 - Reconstructing Data with JOIN
#the JOIN operation links across several tables as part of a 
# select operation

#JOIN needs to know how to use the keys that make connections
#between tables using an ON clause

"""
select Album.title, Artist.name from Album join Artist on 
Album.artist_id = Artist.id
"""

"""
select Track.title, Genre.name from Track join Genre on 
Track.genre_id = Genre.id
"""

"""
select Track.title, Artist.name, Album.title, Genre.name from Track 
join Genre join Album join Artist on Track.genre_id = Genre.id and 
Track.album_id = Album.id and Album.artist_id = Artist.id
"""