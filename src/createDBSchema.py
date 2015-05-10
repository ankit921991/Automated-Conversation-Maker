import json
import sqlite3
import re 

def generateDBSchema():
    """
    This extracts the data from the JSON data which is obtained by using the Facebook graph search API.The sample JSON data can be found at the github repository at : https://github.com/ankit921991/Automated-Conversation-Maker/tree/master/data.This data obtained can be categorisez into following cattegories

1) Personal - Database Table :: PERSON. Fields :: name, birthday, hometown, location 
2) Educational - Database Table :: EDUCATION. Fields :: name, school_name, school_type, school_year
3) Music - Database Table :: MUSIC. Fields :: name, category, music
4) books - Database Table :: BOOKS. Fields :: name, category, books
5) movies - Database Table :: MOVIES. Fields :: name, category, movie
6) sports - Database Table :: SPORT. Fields :: name, sports
7) favorite team - Database Table :: TEAM. MOVIESFields :: name, team
8) favorite athlete - Database Table :: ATHLETE. Fields :: name, athlele
9) Inspirational  people - Database Table :: INS_PEOPLE. Fields :: name, people

This program extracts the data from the JSON file and categorize them into above categorisies. Then the data is inserted into the database into respective tables as shown above.  This data will be used later by virtual humans for communication. Here "name" field is there in all thee tables. Though there is no primary key for any of the table, "name" field virtually acts as a primary key to extract the data
    """
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()

    c.execute("DROP TABLE PERSON")
    c.execute("DROP TABLE EDUCATION")
    c.execute("DROP TABLE ATHLETE")
    c.execute("DROP TABLE TEAM")
    c.execute("DROP TABLE SPORT")
    c.execute("DROP TABLE MUSIC")
    c.execute("DROP TABLE BOOKS")
    c.execute("DROP TABLE MOVIES")
    c.execute("DROP TABLE INS_PEOPLE") 

    c.execute("CREATE TABLE PERSON (name text , birthday text, hometown text, location text)")
    c.execute("CREATE TABLE EDUCATION (name text , school_name text, school_type text, school_year text)")
    c.execute("CREATE TABLE ATHLETE (name text , athlete text)")
    c.execute("CREATE TABLE TEAM (name text , team text)")
    c.execute("CREATE TABLE SPORT (name text , sports text)")
    c.execute("CREATE TABLE MUSIC (name text , category text, music text)")
    c.execute("CREATE TABLE BOOKS (name text , category text, books text)")
    c.execute("CREATE TABLE MOVIES (name text , category text, movie text)")
    c.execute("CREATE TABLE INS_PEOPLE (name text , people text)") ##for inspirationa people

    conn.commit()
    conn.close()

if __name__ == "__main__":
    generateDBSchema()