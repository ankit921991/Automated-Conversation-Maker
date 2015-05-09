import sys
import time
import sqlite3
conn = sqlite3.connect('facebook.db')
c = conn.cursor()
from questionToSQL import extractQuery  
import copy

GLOBAL = 0
semanticDictionary = {'birthday':'entity','name':'entity','education':'entity','athletes':'person','hometown':'entity','music':'adj_entity','sports':'adj_entity','books':'adj_entity','movies':'adj_entity','team':'adj_entity'}
flagDict = {'birthday':0,'name':0,'education':0,'athletes':0,'hometown':0,'music':0,'sports':0,'books':0,'movies':0,'team':0} 


def getAnswer(current_question,questioning_user):
    """
    This takes the current question being asked and the user to which the question is being referred as input.It then calls the extractQuery function from questionToSQL file to get the equivalent SQL queries for the question.It then executes these quesries to get the data from the sqlite database and returns the result back.
    """
    querySet = extractQuery(current_question,questioning_user) 
    for query in querySet:
        print(query)
        resultSet = c.execute(query)
        result = resultSet.fetchone() 
        if result :
            return(str(result[0]))
    #print(querySet)   
    #return querySet
    
def toggle(questioning_user,answering_user):
    temp = questioning_user
    questioning_user = answering_user
    answering_user = temp
    return questioning_user,answering_user
    
def getNextQuestionAndCategory():
    #global GLOBAL
    global semanticDictionary
    global category
    current_category = ""
    current_question = ""
    for key,value in category.items():
        for categ,flag in value.items():
            if flag == 0:
                current_category = categ
                break
        break
    if current_category == "":
        return 'end','end'
    else:
        if semanticDictionary[current_category] == 'entity':
            current_question = 'what is your ' + current_category+' ?'
            return current_question,current_category
        if semanticDictionary[current_category] == 'person':
            current_question = 'who is your ' + current_category+' ?'
            return current_question,current_category
        if semanticDictionary[current_category] == 'adj_entity':
            current_question = 'which is your favourite ' + current_category+' ?'
            return current_question,current_category
        
##def getAnswer(current_question,answering_user):
##    return 'answer'
 
def start():
    global category
    #user_1, user_2 = getUser()
    startup_question = "What is your name?"
    current_question = startup_question
    previous_question_category = ""
    current_question_category = "name"
    
    questioning_user = USER_A
    answering_user = USER_B
    print(questioning_user + " : " + current_question)
    previousAnswer = ""
    while(1):
        answer = getAnswer(current_question,answering_user)
        category[questioning_user][current_question_category] = 1
        if category[answering_user][current_question_category] == 1:
            current_question,current_question_category = getNextQuestionAndCategory()
        if current_question == "end":
            print(answering_user + " : " + answer)
            break
        
        #if (previous_question_category == current_question_category and answer != previousAnswer):
        #    answerPart = current_question.split('your')
        #    NewAnswer = 'My ' + answerPart[1] + ' is '+answer + 'too'
        #    print(answering_user + " : " + NewAnswer + ", "+ current_question)
        #else:
        if answer:
            print(answering_user + " : " + answer + ", "+ current_question)
        else:
            print(answering_user + " : " + current_question)
            time.sleep(1)
        previous_question_category = current_question_category 
        previousAnswer = answer
        questioning_user,answering_user = toggle(questioning_user,answering_user)

if __name__=="__main__":
    USER_A = ""
    USER_B = ""
    USER_A = raw_input('Enter The First User : ')
    USER_B = raw_input('Enter The Second User : ')
    category = {}
    category[USER_A] = copy.copy(flagDict)
    category[USER_B] = copy.copy(flagDict)
    start()




    

