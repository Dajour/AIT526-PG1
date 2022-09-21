'''
Problem: To implement a chatbot that is named Eliza and will engage with the user in the command line.

This file will implement a Chatbot named Eliza. Eliza will be able to have a conversation with the 
user and be able to keep up a conversation until the user breaks the conversation.

Usage instructions:
As the user if Eliza asks you a question please start with your sentence with 'I' this will allow for 
Eliza to give you the best feedback that is needed. 

Example Conversation:
Eliza: Hello 'user', how may I help you today?
User: I am tired
Eliza: Whay are you tired 'user'?
User: Because I got little sleep.

Libraries User:
Regex
NLTK

We used the input function to gather what the user is saying, and with libraries Regex and NLTK we used regex to find some
keywords in the sentence that the user has said and with regex ELiza asks the user more questions with re.sub().
'''


import re
import nltk
import random

def greeting(): # This is the first thing the user will see with Eliza asking for the user's name.
    from nltk.tokenize import word_tokenize
    userName = input("Hi My Name is Eliza, what is your name? ") 
    if userName == '': # If the response was empty we ask the user again for their name.
        userName = input("Don't be shy, what is your name?")
    
    nameList = word_tokenize(userName)  # Tokenize the sentence we get from the user to extract the user's name. should be nameList[3] 
    
    name = nameList[3]
    return name


    # We use re.sub to extract the user's name and then ask them the a question with their name in the sentence.
    firstQuestion = input(re.sub(r'(M|m)y name is (.+)', r'Hi \2. How are you feeling today', userName))
    
    xList = word_tokenize(firstQuestion)
    
    xList = [i.replace('you', 'me')for i in xList]
    
    if xList[0] == 'I' or xList[0] == 'i':
        response = input(re.sub(r'(I|i) (.+) you', nameList[3] + r', Why do you \2?', firstQuestion))
        return response
        
name = greeting()
feelings = [
    [
        r"happy", 
        ["Why do you feel happy?"],
    ],
    [
        r"good",
        ["Why do you feel good?"],
    ],
    [
        r"sad",
        ["What has made you sad"],
    ],
    [
        r"mad",
        ["How can I make you feel better?"],
    ],
    [
        r"sick",
        ["What do you think made you sick? "],
    ]
]
    




def conversation(name):
    from nltk.tokenize import word_tokenize
    
    firstQuestion = input("Hello " + name + ", How are you feeling today")
    fqToken = word_tokenize(firstQuestion)
    while True:
        for key in feelings:
            if key[0] == fqToken[2]:
                nextQuestion = key[1][0]
                nextQuestion = input(nextQuestion + "OR Type 'quit' to end")
       
       
        if nextQuestion == 'quit':
            break
        
    print('Your conversation has ended, thank you!!!')
    
conversation(name)
   
 
    
    
