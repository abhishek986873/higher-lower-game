import pyfiglet
import random

# -------------------------------------------------------------------------------------------------------------------------------

# function -1 / to print  heading of the game as [HIGHER LOWER GAME]

def heading(x,y,z):  # x = heading of game its depend on you what you want to call ,y =  font name
    ascii_code = pyfiglet.figlet_format(x, font=y,width=z)
    print(ascii_code)
    print('-' * 80)

# calling function - 1
heading("HIGHER  LOWER GAME" , 'standard',50)

#----------------------------------------------------------------------------------------------------------------------------------------------

# function - 2  creating two dictionary 1st contain 12 stars with insta followers and 2nd dictionary with 12 other followers and we compare them by taking randomly

DICT1 = {
    "⚫ SHARUKH KHAN":37,
    "⚫ RANVEER KAPOOR":2.4,
    "⚫ DEEPIKA PADUKON":33,
    "⚫ VIRAT KOHLI":244,
    "⚫ TAYLOR SWIFT":253,
    "⚫ ASHISH CHANCHLANI":14,
    "⚫ AMIT BACDANA ":9,
    "⚫ RONALDO":573

}

#-------------------------------------------------------------------------------------------------------------------------------------------------------

DICT2 = {
    "⚫ SALMAN KHAN":60,
    "⚫ RANVEER SINGH": 43,
    "⚫ PRIYANKA CHOPRA":86,
    "⚫ DHONI":41,
    "⚫ ARJIT SINGH":7,
    "⚫ BHUVAM BAM":16,
    "⚫ HARSH BENIWAL":6,
    "⚫ MESSI": 453

}

#-------------------------------------------------------------------------------------------------------------------------------------
# function -3  definig a function that will select a random celibrity from both the dictionary

def random_celibrity(dictionary):
    return random.choice(list(dictionary.keys()))


#-----------------------------------------------------------------------------------------------------------------------------

#function-4 defining a function that will take the user input

def take_input():

    while True:
        print("WHICH CELIBRITY HAS HIGHEST FOLLOWER ?")
        ask = input("⚫ ENTER YOUR CHOICE ? [ 1 OR 2 ] = ")
        if ask != "1" and ask != "2":
            print("ENTER A VALID INPUT ONLY [1 OR 2]")
            print("-"*69)

        else:
            print("-"*69)
            break
    return ask

# -----------------------------------------------------------------------------------------------------------------------------------
score = 0 # creating the variable that take cout of score



the_end = 0 # creating a special variable that take care that it os always 0 and when ever player loose the game it increase by 1 and when it become 1 loop get terminate


#----------------------------------------------------------------------------------------------------------------------------
# function -5 this function will check whether user input the right option and do others stuffs

def wright_or_wrong():
    global score
    global the_end
    celibrity1 = random_celibrity(DICT1)  # taking random celibrity from dict1

    celibrity2 = random_celibrity(DICT2)  # taking random celibrity from dict2

    heading(celibrity1,"standard",120)   # creating big heading of celibrity 1

    heading('VS',"standard",180)            # creating big heading of VS

    heading(celibrity2,"standard",120)   #  creating big heading of celibrity 2

    ask = take_input()

    if ask == '1' and DICT1[celibrity1]>DICT2[celibrity2]:
        print("⚫ YES YOU ARE RIGHT \n⚫ YOU WON")

        score = score+1
        print(f"⚫ YOUR SCORE = {score}")
        print("-"*69)

    elif ask == '2' and DICT2[celibrity2]>DICT1[celibrity1]:
        print("⚫ YES YOU ARE RIGHT \n⚫ YOU WON")

        score = score+1
        print(f"⚫ SCORE =  {score}")
        print("-"*69)
    else:
        print("⚫ YOU LOOSE THE GAME")

        the_end = the_end+1





#-------------------------------------------------------------------------------------------------------------------------------


# end game

while True:
    wright_or_wrong()
    if the_end == 1:
        break

