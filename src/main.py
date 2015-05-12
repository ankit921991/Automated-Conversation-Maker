import sys
import time
import sqlite3
conn = sqlite3.connect('facebook.db')
c = conn.cursor()
from questionToSQL import extractQuery  
import copy


GLOBAL = 0
semanticDictionary = {'birthday':'entity','name':'entity','school name':'entity','athletes':'person','hometown':'entity','music':'adj_entity','sports':'adj_entity','books':'adj_entity','movies':'adj_entity','team':'adj_entity'}
flagDict = {'birthday':0,'name':0,'school name':0,'athletes':0,'hometown':0,'music':0,'sports':0,'books':0,'movies':0,'team':0} 


def getAnswer(current_question,questioning_user):
    """
    This takes the current question being asked and the user to which the question is being referred as input.It then calls the extractQuery function from questionToSQL file to get the equivalent SQL queries for the question.It then executes these quesries to get the data from the sqlite database and returns the result back.
    """
    querySet = extractQuery(current_question,questioning_user) 
    for query in querySet:
        #print(query)
        resultSet = c.execute(query)
        result = resultSet.fetchone() 
        if result :
            return(str(result[0]))
    #print(querySet)   
    #return querySet
    
def toggle(questioning_user,answering_user):
    """
    This function toggles the the user who is currently answering the question with the user who is currently asking the question. It simply swaps the answering user with the questioning user
    """
    temp = questioning_user
    questioning_user = answering_user
    answering_user = temp
    return questioning_user,answering_user
    
def getNextQuestionAndCategory():
    """
    We have different categories like movie, sport, music. This function chooses the category which is not covered till now and checks whether the semantic type of the category is person or entity and accordingly create question for the same category. This function returns the new question and category.
    Example: If the category which is not used till now is home town this function checks for its semantic type which is entity hence the next question prepared is :: what is your hometown?
    """
    
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
        #if semanticDictionary[current_category] == 'adj_person':
        #    current_question = 'who is your favorite ' + current_category+' ?'
        #    return current_question,current_category
        if semanticDictionary[current_category] == 'adj_entity':
            current_question = 'which is your favourite ' + current_category+' ?'
            return current_question,current_category

def start():
    result=[]
    """
    This is the starter program which runs the main Algorithm. The algorithm developed is as follows :: 
    DEVELOPE THE ALGORITHM
    """
    global category
    #user_1, user_2 = getUser()
    startup_question = "What is your name?"
    
    current_question = startup_question
    previous_question_category = ""
    previousAnswer = ""    
    current_question_category = "name"
    questioning_user = USER_A
    answering_user = USER_B
    print(questioning_user + " : " + current_question)
    result.append(questioning_user + " : " + current_question)
    previousAnswer = ""
    while(1):
        answer = getAnswer(current_question,answering_user)
        category[questioning_user][current_question_category] = 1
        #previous_question_category = current_question_category
        #previousAnswer = answer
        if category[answering_user][current_question_category] == 1:
            current_question,current_question_category = getNextQuestionAndCategory()
        if current_question == "end" and answer:
            result.append(answering_user + " : " + answer)
            print(answering_user + " : " + answer)
            break
        
        #if (previous_question_category == current_question_category and answer != previousAnswer):
        #    answerPart = current_question.split('your')
        #    NewAnswer = 'My ' + answerPart[1] + ' is '+answer + 'too'
        #    print(answering_user + " : " + NewAnswer + ", "+ current_question)
        #else:
        if answer:
            print(answering_user + " : " + answer + ", "+ current_question)
            result.append(answering_user + " : " + answer + ", "+ current_question)
        else:
            result.append(answering_user + " : " + current_question)    
            print(answering_user + " : " + current_question)
        #time.sleep(1)
        questioning_user,answering_user = toggle(questioning_user,answering_user)
    return result

if __name__=="__main__":
    """
    This is the main function. It takes as input two users and builds the category dictionary for both the users. This then call start function
    """
    USER_A = ""
    USER_B = ""
    USER_A = raw_input('Enter The First User : ')
    USER_B = raw_input('Enter The Second User : ')
    category = {}
    category[USER_A] = copy.copy(flagDict)
    category[USER_B] = copy.copy(flagDict)
    result = []
    result = start()
    iterator = 0
    print("*************************CONVERSATION******************************")
    for entry in result:
        print(entry)
        iterator+=1
        if iterator%2 == 0:
            time.sleep(5)
    




    

