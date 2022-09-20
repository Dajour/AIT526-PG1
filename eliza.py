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

def greeting(): # This is the first thing the user will see with Eliza asking for the user's name.
    
        userName = input("Hi My Name is Eliza, what is your name? ")
        if userName == '':
            userName = input("Don't be shy, what is your name?")
            
        x = input(re.sub(r'My name is (.+)', r'Hi \1. How can I help you today', userName))
        return x
        
firstQuestion = greeting()
print(firstQuestion)

