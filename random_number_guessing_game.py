import math
import random

#Taking inputs
lower=int(input("enter the lower bound:"))
upper=int(input("enter the upper bound:"))

#generating a random number
x=random.randint(lower,upper)

#minimum number of chances to guess
min_guesses=round(math.log(upper-lower+1,2))
print("you have only ",min_guesses," chances to guess")

# Initializing the number of guesses.
count=0

# for calculation of minimum number of
# guesses depends upon range
while count <= min_guesses:
    count+=1

    #enter the guessing number
    guess=int(input("enter the guessing number:"))

     # Condition testing
    if x == guess:
        print("<----congratulations---->")
        print(" you have guessed in ",count," try")

        print("The number is ",x)

         # Once guessed, loop will break
        break
    elif x > guess:
        print("you guessed too small")
    elif x < guess:
        print("you guessed too high")
    
# If Guessing is more than required guesses,
# shows this output.
if count > min_guesses:
    print("<----Better Luck Next Time---->")
    print("you didn't guesssed in minimum number of guesses")
    print("The number is ",x)
    
