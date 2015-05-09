import json
import sqlite3
import re 
conn = sqlite3.connect('facebook.db')
c = conn.cursor()

'''
c.execute("DROP TABLE PERSON")
c.execute("DROP TABLE EDUCATION")
c.execute("DROP TABLE ATHLETE")
c.execute("DROP TABLE TEAM")
c.execute("DROP TABLE SPORT")
c.execute("DROP TABLE MUSIC")
c.execute("DROP TABLE BOOKS")
c.execute("DROP TABLE MOVIES")
c.execute("DROP TABLE INS_PEOPLE") ##for inspirationa people

#NEW SCHEMA:

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

'''

#'''
with open('final.json') as data_file:    
    data = json.load(data_file)

##general data variables
birthday = name = hometown = location = ""


##education data
school_name = school_type = school_year = ""


##favourite_athlete data
favourite_athlete = ""


##favourite_team data
favourite_team = ""


##sports data
sport = ""


##music data
music_category = music_name = ""



##boooks data
books_category = books_name = ""


##movies data
movies_category = movies_name = ""



##inspirational_people data
inspirational_people = ""


#c.execute("CREATE TABLE MOVIES (name text , category text, movies_name text)")
data = data['data']
for records in data:
    ##general data
    if 'birthday' in records:
        birthday = records['birthday'] 
        #birthday = re.sub('\'','',birthday)
    if 'name' in records:
        name = records['name']
        name = re.sub('\'','',name)
    if 'hometown' in records:
        hometown = records['hometown']['name']
        hometown = re.sub('\'','',hometown)
    if 'location' in records:
        location = records['location']['name']
        location = re.sub('\'','',location)
        
    ##CREATE TABLE PERSON (name text , birthday text, hometown text, location text)
    query = 'insert into person values(' + '\''+str(name)+'\'' + ',' +'\''+str(birthday) +'\''+ ',' + '\''+str(hometown) + '\''+',' + '\''+str(location)+ '\''+')'
    print(query)
    c.execute(query)    
    
    ##Education data 
    if 'education' in  records:
        for education in records['education']:
            if 'school' in education:
                school_name = education['school']['name']
                school_name = re.sub('\'','',school_name)
            if 'type' in education:
                school_type = education['type']
                school_type = re.sub('\'','',school_type)
            if 'year' in education:
                school_year = education['year']
                #school_year = re.sub('\'','',school_year)
            ##CREATE TABLE EDUCATION (name text , school_name text, school_type text, school_year text)
            query = 'insert into education values('+ '\''+str(name) +'\''+ ',' + '\''+str(school_name) +'\''+ ',' + '\''+str(school_type) +'\''+ ',' + '\''+str(school_year) +'\''+ ')'
            c.execute(query)        
            print(query)
    ##favourite_athlete            
    if 'favorite_athletes' in records:
        for athletes in records['favorite_athletes']:
            favourite_athlete = athletes['name']
            favourite_athlete = re.sub('\'','',favourite_athlete)
            ##CREATE TABLE ATHLETE (name text , athlete text)    
            query = 'insert into athlete values(' + '\''+name +'\''+ ',' + '\''+favourite_athlete +'\''+')'
            c.execute(query)    
            print(query)
    ##favourite_team
    if 'favorite_teams' in records:
        for teams in records['favorite_teams']:
            favourite_team = teams['name']
            favourite_team = re.sub('\'','',favourite_team)
            ##CREATE TABLE TEAM (name text , team text)
            query = 'insert into team values(' + '\''+name + '\''+',' + '\''+favourite_team +'\''+')'
            c.execute(query)        
            print(query)
    
    ##sports
    if 'sports' in records:
        for sports in records['sports']:
            sport = sports['name']
            sport = re.sub('\'','',sport)
            query = 'insert into sport values(' + '\''+name + '\''+',' + '\''+sport +'\''+')'
            ##CREATE TABLE SPORT (name text , sports text)
            c.execute(query)    
            print(query)
    
    ##music
    if 'music' in  records:
        for musics in records['music']['data']:
            if 'category' in musics:
                music_category = musics['category']
                music_category = re.sub('\'','',music_category)
            if 'name' in musics:
                music_name = musics['name']
                music_name = re.sub('\'','',music_name)
            ##CREATE TABLE MUSIC (name text , category text, music_name text)
            query = 'insert into music values(' + '\''+name + '\''+',' +'\''+music_category +'\''+','+'\''+music_name +'\''+')'
            c.execute(query)    
            print(query)
    
    ##boooks
    if 'books' in  records:
        for books in records['books']['data']:
            if 'category' in books:
                books_category = books['category']
                books_category = re.sub('\'','',books_category)
            if 'name' in books:
                books_name = books['name']
                books_name = re.sub('\'','',books_name)
            ##CREATE TABLE BOOKS (name text , category text, books_name text)
            query = 'insert into books values(' + '\''+name+ '\''+ ',' + '\''+books_category+'\'' +','+'\''+books_name +'\''+')'
            c.execute(query)
            print(query)
    
    ##movies
    if 'movies' in  records:
        for movies in records['movies']['data']:
            if 'category' in movies:
                movies_category = movies['category']
                movies_category = re.sub('\'','',movies_category)
            if 'name' in movies:
                movies_name = movies['name']
                movies_name = re.sub('\'','',movies_name)
            ##CREATE TABLE MOVIES (name text , category text, movies_name text)
            print(name +'\''+ ',' +'\''+ movies_category+'\''+ ',' +'\''+movies_name)
            query = 'insert into movies values(' + '\''+name +'\''+ ',' +'\''+ movies_category+'\''+ ',' +'\''+movies_name+'\''+ ')'
            c.execute(query)    
            print(query)
            
    ##inspirational_people
    if 'inspirational_people' in records:
        for people in records['inspirational_people']:
            inspirational_people = people['name']
            inspirational_people = re.sub('\'','',inspirational_people)
            print(inspirational_people)
            query = 'insert into ins_people values(' + '\''+name +'\''+ ',' +'\''+ inspirational_people +'\''+ ')'
            ##CREATE TABLE INS_PEOPLE (name text , people text)
            c.execute(query)
            print(query)

conn.commit()
conn.close()
#'''