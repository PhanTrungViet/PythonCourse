#use random list to random question value and tastes value
import random

#Build 2 dictionaries
questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#function ask and reply
def Ingredient():
    #get random key from question dictionaries
    random_question = random.choice(list(questions.keys()))
    #print corresponding question
    print(questions[random_question])
    #get input value from user
    tastes = input()
    #compare tastes value with key question
    if(tastes == random_question):
        #print resulf
        print(random.choice(ingredients[tastes]))
    else:
        print("wrong")

def Ingredient2():
    for key in questions:
        print(questions[key])
        reply = input()
        if(reply == "Y" or reply == "y" or reply.lower() == "yes"):
            print(random.choice(ingredients[key]))
            break
        elif(reply == "N" or reply == "n" or reply.lower() == "no"):
            continue


#Ingredient()
Ingredient2()