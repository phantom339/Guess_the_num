from funcs import num_gen
from funcs import num_comp
import art

play="y"
while play=="y":
    print(art.logo)
    lvl=input("Would you like to play on Hard lvl or on Easy lvl: H/E ").lower()
    if lvl=="h":
        lives=5
        c_num=num_gen()
        print(c_num)
        #maybe while loop should be introduced here:
        while lives>0:
            p_num=int(input("Guess a number between 1-100:(including the end points too: )"))
            #here the comparision function is called:
            res=num_comp(num1=c_num, num2=p_num)
            lives-=1
            print(f"{res} \n Lives left: {lives}")
            if res=="You Guessed the correct number.":
                lives=0
    
    elif lvl=="e":
        lives=10
        c_num=num_gen()
        print(c_num)
        #maybe while loop should be introduced here:
        while lives>0:
            p_num=int(input("Guess a number between 1-100:(including the end points too: )"))
            #here the comparision function is called:
            res=num_comp(num1=c_num, num2=p_num)
            lives-=1
            print(f"{res} \n Lives left: {lives}")
            if res=="You Guessed the correct number.":
                lives=0
   
    play=input("Would you like to play Guess the Number again: Y/N ").lower()
print(art.thanks)    