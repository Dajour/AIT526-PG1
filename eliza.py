'''
Problem: To implement a chatbot that is named Eliza and will engage with the user in the command line.

This file will implement a Chatbot named Eliza. Eliza will be able to have a conversation about the users feeling 
and be able to keep up a conversation until the user breaks the conversation.


Usage Instructions:
When Eliza asks for your name please use the format:
    'My name is _________ ' - this will allow Eliza to take your name correctly
    
When Eliza asks 'how are you feeling' please use the format:
    'I feel _______' - this will allow for eliza to provide the feedback for you as the user.
    The current feelings that Eliza recognizes are:
        happy
        good
        sad
        mad
        sick
        healthy
        bad
        alright
        great
        
    If you don't say these feelings, Eliza will ask for you to simplify your feelings
    
    If you still can't simplify your feelings the conversation will be ended.
    
    Once you have said your feeling, please start next question with:
        'Because ________' - this will once again allow Eliza to say a appropriate repsonse
        
    Once you answer this question, Eliza will ask if you want to explore your feelings more and will ask
    'How you are feeling?' again
    
    If at anytime you want to quit just type 'quit'
     

Example Conversation:
Eliza: 'Hi my name is Eliza, what is your name?
User: 'My name is user
Eliza: Hello user, how are you feeling today?
User: I feel good
Eliza: Why do you feel good?
User: Because I got promoted at work.
Eliza: Why don't you tell me more about your work?

Libraries User:
Regex
NLTK

We used the input function to gather what the user is saying, and with libraries Regex and NLTK we used regex to find some
keywords in the sentence that the user has said and with regex ELiza asks the user more questions with re.sub().
'''


import re
import nltk
import random

# This is the function that the user will see with Eliza asking for the user's name.
def greeting(): 
    from nltk.tokenize import word_tokenize
    userName = input("Hi My Name is Eliza, what is your name? ") 
    if userName == '': # If the response was empty we ask the user again for their name.
        userName = input("Don't be shy, what is your name?")
    
    nameList = word_tokenize(userName)  # Tokenize the sentence we get from the user to extract the user's name. should be nameList[3] 
    
    name = nameList[3] # set name to the name of the user in give input 'My name is userName' 
    return name # return name to be used in conversation.
        
name = greeting()

# These are the feelings that Eliza understands and will ask more questions about
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
        ["When did you start to feel this way?"],
    ],
    [
        r"bad",
        ["How can I make you feel better?"],
    ],
]
    


# This is the function that the main conversation will be held
# If the conversation is ended by the user typing 'quit' then this
# function will be ended.
def conversation(name):
    from nltk.tokenize import word_tokenize
    
    firstQuestion = input("Hello " + name + ", How are you feeling today")
    fqToken = word_tokenize(firstQuestion) # tokenize this sentence to extract the feeling that the user has.
    while True :
        feelingFound = False # this variable will tell Eliza if she knows the feeling that the user has said they have
        
        # loop through all the feelings that Eliza recognizes to check if the user inputted
        # feeling matches.
        for key in feelings: 
            if key[0] == fqToken[2]: # If there is a match, you get the response that is corrrelated with that feeling and ask next question.
                nextQuestion = key[1][0]
                nextQuestion = nextQuestion + " OR Type 'quit' to end"
                feelingFound = True
                
        # Variable to keep track if user wants to be asked more questions
        keepGoing = False
    
        if feelingFound == True:
            question = input(nextQuestion)       
        
        # Check to see if the feeling that user inputted is found, if not ask new question
        # Once the user is asked the question, check feelings again to see if the simplified feeling 
        # can be found. If not then ask the user to quit.
        if feelingFound == False:
            nextQuestion = input("Sorry " + name + " i don't understand your feeling please simplify OR type 'quit' to end")
            for key in feelings:
                if key[0] == fqToken[2]:
                    nextQuestion = key[1][0]
                    nextQuestion = input(nextQuestion + " OR Type 'quit' to end")
                    feelingFound = True
        
        nextQuestion = input("Sorry I can't help you. Please type 'quit' to end our conversation")
         
        if nextQuestion == 'quit':
            break
        
    print('Your conversation has ended, thank you!!!')
    
conversation(name)
   
 
    
    
