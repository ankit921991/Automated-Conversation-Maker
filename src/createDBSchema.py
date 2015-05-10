import json
import sqlite3
import re 

def generateDBSchema():
    """
    This function drops the tables if they are already present and then generates them from the respective create table commands.The databse used is sqlite3
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