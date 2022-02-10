import random
import time
def roll(inp):
    di=["⚀","⚁","⚂","⚃","⚄","⚅"]
    if(inp=="y"):
        num=random.randint(0,5)
        for i in range(0,5):
            if(i==num):
                print(di[i])
    else:
        time.sleep(60) 
        print("what are you wating for?")
        time.sleep(604800) 
        print("WHY DID YOU HAVT THIS RUNNING FOR A WEEK ")
        time.sleep(31540000) 
        print("A YEAR HAS PASED AND YOU ARE STILL WATING!?!?!?!?! OK FINE YOU CAN ROLL AGAIN")
for i in range(1,100):
    ye=input("y to roll n to stop playing: ")
    roll(ye)
