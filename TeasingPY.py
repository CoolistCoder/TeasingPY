"""
    A fun little demo that teases the user.  Written in Python 3
"""
import random
from datetime import datetime


#randomize the seed 
random.seed(datetime.now())

#output the prompt
print("Hello, I'm going to tease you!  Type 'stop it' to stop the teasing.")
userin = ""                     #this will be used to take input
while (userin != "stop it"):                #exit condition is "stop it"
    userin = input("Tell me something: ")   #take input here
    if userin == "stop it":             #we want to check and see if the user said stop before we execute code
        break       #simply break the loop

    response = random.randint(0,3)      #randomly choose one of four options
    
    if (response == 0):                 #at 0, reverse the string
        usermod = userin[::-1]          #save the user's input in reverse
        print(usermod);                 #print out the modified input
    elif (response == 1):               #at 1, we count the number of characters in the string
        usermod = userin                #save our input to the usermod buffer
        print(usermod + " is a sentence just " + str(len(usermod)) + " letters too long!") #just output the length of the string with a funny little message
    elif (response == 2):               #at 2, our string is stuttered 
        usermod = userin                #save the user's input to the mod buffer
        for i in range(0, len(usermod)):#iterate through the modified buffer
            for j in range(random.randint(1, 6)):   #randomly output multiples of the same character
                print(usermod[i], end = "") #print all of these characters out on the same line
        print("")
    elif (response == 3):               #at 3, our string will be converted to uppercase
        usermod = userin.upper()        #save the user's input as uppercase letters to the mod buffer
        print("How about I scream what you said: " + usermod)   #output the uppercase string but with funny text to go along with it

print("I'm sorry, have a great day c:")    #last print tells us that our program has exited perfectly