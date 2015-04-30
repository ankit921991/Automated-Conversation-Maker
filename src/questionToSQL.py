import sys
import os
import re

##call the stanford dependancy parser and return the result
def parseFile(filename):
    outfile = 'out.txt'
    command = r'java -mx1200m -cp "/home/ankit/Desktop/stanford-parser-full-2015-01-30/stanford-parser.jar:" edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "typedDependencies" /home/ankit/Desktop/stanford-parser-full-2015-01-30/stanford-parser-3.5.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz ' + filename +' > '+outfile #command to use stanford parser 
    os.system(command) ##execute command
    return outfile


##this function is for future purpose. In future if we need to map from the key to its meaning and 
##then to the field in database then this function can be used
def getEquivalent(key):
    ##return key
    
    ##synonym list for books
    books = ['book','novel']
    ##synonym list for sports
    sports = ['game','sport']
    ##synonym list for movies
    movies = ['film','movie']
    ##synonym list for music
    musics  = ['song','music']
    ##synonym list for favorite_athlete
    favorite_athlete = ['player','athlete']
    
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
            return 'moview'
        
    ##check for music category
    for keys in music:
        if keys in key:
            return 'music'
        
    ##check for favorite_athlete category
    for keys in favorite_athlete:
        if keys in key:
            return 'favorite_athlete'
    
#------------------------------------------------------------------------------------------------


##this function will return query for the questions starting from what
##Ex : what is your name?
def extractWhat(lines,question,user):
    nn = ""  
    nsubj = ""
    #print(lines)
    #lines = lines.split()
    for line in lines:
        print(line)
        if 'nsubj' in line:
            nsubj = line[13:len(line)-4]
            #print(nsubj)
        if 'nn' in line:
            nn = line[10:len(line)-3]
    ##key = getEquivalent(nsubj +" " + nn)
    key = nsubj + nn
    return('select ' + key + ' from table where username = ' + user)
        
##this function will return query for the questions starting from who
##Ex : who is your favorite athlete?
def extractWho(lines,question,user):
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
    return('select ' + key + ' from table where username = ' + user)
    
##this function will return query for the questions starting from which
##Ex : which book do you like?
##Ex : which is your favorite book?
def extractWhich(lines,question,user):
    det= ""
    amod = ""
    key = ""
    print(lines)
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
    return('select ' + key + ' from table where username = ' + user)

##this function will return query for the questions starting from which
#def extractwhere(lines,question,user):
#    return ""


##this is to extract query depending upon whether question is starting from what, where, who, when, why
##which etc. This can be expanded as the scope of the project expands
def extractQuery(lines,question,user):
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
    f = open('temp.txt','w')
    f.write(question)
    f.close()
    outfile = parseFile('temp.txt')
    f = open(outfile,'r')
    lines = f.readlines()
    query = extractQuery(lines,question,user)
    print(query)
    #executeQuery(query)