import re
import nltk

userName = input("Hi My Name is Eliza, what is your name? ")
if userName == '':
    userName = input("Dont be shy, what is your name? ")

first_response = input("Hello " + userName + " how may I help you today?")

x = re.sub(r'I am (.+)', r'Why are you \1?', first_response)

print(x)

