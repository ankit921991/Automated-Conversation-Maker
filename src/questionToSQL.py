import sys
import os
import re

schemaDict = {'PERSON' : ['name' , 'birthday', 'hometown', 'location'],'EDUCATION':['name' , 'school_name', 'school_type', 'school_year'],'ATHLETE' :['name', 'athlete'],'TEAM' :['name'  , 'team'],'SPORT' :['name'  , 'sports'], 'MUSIC' :['name'  , 'category' , 'music'],'BOOKS' :['name'  , 'category' , 'books'],'MOVIES' :['name'  , 'category' , 'movie'],'INS_PEOPLE' :['name'  , 'people']}

def parseFile(filename):
    """
    This function uses JAVA API for stanford dependacy parser to parse the question and produce typed dependacies. These dependacies can be latter use to extract the important information from the question such as subject, object type of question etc.
    """
    outfile = 'out.txt'
    command = r'java -mx1200m -cp "/home/ankit/Desktop/stanford-parser-full-2015-01-30/stanford-parser.jar:" edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "typedDependencies" /home/ankit/Desktop/stanford-parser-full-2015-01-30/stanford-parser-3.5.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz ' + filename +' > '+outfile #command to use stanford parser 
    os.system(command) 
    return outfile

def getEquivalent(key):
    """
    A single word can have multiple synonym Example athlete can be called player, sportsperson etc. in the question these various synonyms can be used but the database table has only one name Example: table for athelete is Athlete. So, even though different synonym are used the query shuold be for a single table. This function simply returns the equivalent word for the given key.
    """
    
    ##synonym list for books
    books = ['book','novel','books']
    ##synonym list for sports
    sports = ['game','sport','sports']
    ##synonym list for movies
    movies = ['film','movie','movies']
    ##synonym list for music
    music  = ['song','music']
    ##synonym list for favorite_athlete
    favorite_athlete = ['player','athlete','favorite_athlete']
    
    ##check for books category
    for keys in books:
        if keys in key:
            return 'books'
        
    ##check for sports category
    for keys in sports:
        if keys in key:
            return 'sports'
        
    ##check for movies category    
    for keys in movies:
        if keys in key:
            return 'movie'
        
    ##check for music category
    for keys in music:
        if keys in key:
            return 'music'
        
    ##check for favorite_athlete category
    for keys in favorite_athlete:
        if keys in key:
            return 'athlete'
    
#------------------------------------------------------------------------------------------------


##this function will return query for the questions starting from what
##Ex : what is your name?
def extractWhat(lines,question,user):
    """
    This question takes as input the output of dependancy parser, question and user to which question is asked for all the questions starting with what. It returns the SQL statement to retrieve the respective data from the database.
    """
    tableNames = ['PERSON', 'EDUCATION', 'ATHLETE', 'TEAM', 'SPORT', 'MUSIC', 'BOOKS', 'MOVIES', 'INS_PEOPLE']
    nn = ""  
    nsubj = ""
    #print(lines)
    #lines = lines.split()
    for line in lines:
        #print(line)
        if 'nsubj' in line:
            nsubj = line[13:len(line)-4]
            #print(nsubj)
        if 'nn' in line:
            nn = line[10:len(line)-4]
    ##key = getEquivalent(nsubj +" " + nn)
    #key = nsubj + nn
    if nn:
        key = nn +'_'+nsubj
    else:
        key = nsubj
    key = re.sub('\s+','',key)
    resultQueries = []
    for tableName,columnNameList in schemaDict.items():
        for columns in columnNameList:
            if key == columns:  
                query = 'select ' + key + ' from '+ '\''+tableName+'\'' +' where name = ' + '\''+user+'\''
                resultQueries.append(query)
                break
    return(resultQueries)
        
##this function will return query for the questions starting from who
##Ex : who is your favorite athlete?
def extractWho(lines,question,user):
    """
    This question takes as input the output of dependancy parser, question and user to which question is asked for all the questions starting with who. It returns the SQL statement to retrieve the respective data from the database.
    """
    tableNames = ['PERSON', 'EDUCATION', 'ATHLETE', 'TEAM', 'SPORT', 'MUSIC', 'BOOKS', 'MOVIES', 'INS_PEOPLE']
    amod = ""
    nsubj = ""
    amod = key = ""
    l=0
    for line in lines:
        if 'nsubj' in line:
            nsubj = line[13:len(line)-4]
        l = len(nsubj)+3
    for line in lines:
        if 'amod' in line:
            amod = line[(5+l):len(line)-4]
    key = getEquivalent(amod+"_"+nsubj)
    ##key = amod + "_" + nsubj
    resultQueries = []
    for tableName,columnNameList in schemaDict.items():
        for columns in columnNameList:
            if key == columns:  
                query = 'select ' + key + ' from '+ '\''+tableName+'\'' +' where name = ' + '\''+user+'\''
                resultQueries.append(query)
                break
    return(resultQueries)
    
##this function will return query for the questions starting from which
##Ex : which book do you like?
##Ex : which is your favorite book?
def extractWhich(lines,question,user):
    """
    This question takes as input the output of dependancy parser, question and user to which question is asked for all the questions starting with which. It returns the SQL statement to retrieve the respective data from the database.
    """
    tableNames = ['PERSON', 'EDUCATION', 'ATHLETE', 'TEAM', 'SPORT', 'MUSIC', 'BOOKS', 'MOVIES', 'INS_PEOPLE']
    det= ""
    amod = ""
    key = ""
    #print(lines)
    for line in lines:
        line = re.sub('\n','',line)
        if 'det' in line:
            det = line[4:len(line)-12]
            det = re.sub('[0-9-]','',det)
            break
        if 'amod' in line:
            line = line[5:len(line)-1]
            line = line.split(',')
            amod = line[1]+'_'+line[0]
            amod = re.sub('[0-9-]','',amod)
            break
    if det == "":
        key = getEquivalent(amod)
    elif amod=="":
        key = getEquivalent(det)
        
    resultQueries = []
    for tableName,columnNameList in schemaDict.items():
        for columns in columnNameList:
            if key == columns:  
                query = 'select ' + key + ' from '+ '\''+tableName+'\'' +' where name = ' + '\''+user+'\''
                resultQueries.append(query)
                break
    return(resultQueries)

##this function will return query for the questions starting from which
#def extractwhere(lines,question,user):
#    return ""


##this is to extract query depending upon whether question is starting from what, where, who, when, why
##which etc. This can be expanded as the scope of the project expands
def extractQuery(question,user):
    """
    This function check for the  question type i.e whether question is starting from what, who or which and depending on the question type calls extractWhat, extractWho or extractWhich respectively.
    """
    f = open('temp.txt','w')
    f.write(question)
    f.close()
    outfile = parseFile('temp.txt')
    f = open(outfile,'r')
    lines = f.readlines()
    question_list = question.split()
    if question_list[0].lower()=="where":
        return(extractWhere(lines,question,user))
    elif question_list[0].lower()=="what":
        return(extractWhat(lines,question,user))
    elif question_list[0].lower()=="which":
        return(extractWhich(lines,question,user))
    elif question_list[0].lower()=="who":
        return(extractWho(lines,question,user))
        
        

if __name__ == "__main__":
    if(len(sys.argv)!=3) :
        print('usage: python question user_name')
        sys.exit(0)
    question = sys.argv[1]
    user = sys.argv[2]
    query = extractQuery(question,user)
    print(query)
    #executeQuery(query)