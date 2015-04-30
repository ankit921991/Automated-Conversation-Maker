import sys
import time

GLOBAL = 0
semanticDictionary = {'birthday':'entity','name':'entity','education':'entity','athletes':'person','hometown':'entity','music':'adj_entity','sports':'adj_entity','books':'adj_entity','movies':'adj_entity','team':'adj_entity'}
category = {'A':{'birthday':0,'name':0,'education':0,'athletes':0,'hometown':0,'music':0,'sports':0,'books':0,'movies':0,'team':0},'B':{'birthday':0,'name':0,'education':0,'athletes':0,'hometown':0,'music':0,'sports':0,'books':0,'movies':0,'team':0}}

def getAnswer(current_question,questioning_user):
    return"answer"
    
def toggle(questioning_user,answering_user):
    temp = questioning_user
    questioning_user = answering_user
    answering_user = temp
    return questioning_user,answering_user
    
def getUser():
    return 'A','B'

#def getCategory():
#    category = {'A':{'birthday':0,'name':0,'education':0,'favourite_athletes':0,'hometown':0,'music':0,'sports':0,'books':0,'movies':0,'favourite_team':0},'B':{'birthday':0,'name':0,'education':0,'favourite_athletes':0,'hometown':0,'music':0,'sports':0,'books':0,'movies':0,'favourite_team':0}}
#    return category

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
        
def getAnswer(current_question,answering_user):
    return 'answer'
 
def start():
    global category
    user_1, user_2 = getUser()
    startup_question = "What is your name?"
    current_question = startup_question
    current_question_category = "name"
    
    questioning_user = user_1
    answering_user = user_2
    print(questioning_user + " : " + current_question)
    while(1):
        answer = getAnswer(current_question,answering_user)
        time.sleep(1)
        category[questioning_user][current_question_category] = 1
        if category[answering_user][current_question_category] == 1:
            current_question,current_question_category = getNextQuestionAndCategory()
        if current_question == "end":
            print(answering_user + " : " + answer)
            break
        print(answering_user + " : " + answer + ", "+current_question)
        questioning_user,answering_user = toggle(questioning_user,answering_user)

if __name__=="__main__":
    start()




    

