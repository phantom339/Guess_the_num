import random

def num_gen():
    num=random.randint(1,100)
    return num

def num_comp(num1,num2):
    if num2>100:
        result="Invalid Choice"
        return result
    elif num2>num1:
        result="Your Guess is greater than the Real number."
        return result
    elif num2<num1:
        result="Your is smaller than the Real number."
        return result
    else:
        result="You Guessed the correct number."
        return result
    

