#user needs to type their name to start the game.
print("IN ORDER FOR THIS GAME TO BEGIN...")
name = input("Please type your name: ")


def welcome():#Welcomes the User to the game
    print("Welcome to the Island Game!")
    print("Hello,", name,"! Welcome and now let's go to the customizing station!")

def avatar1():#describes avatar 1
    print("Avatar 1")
    print("They are an outgoing person. They love to talk and make friends. Their only pet peeve is silence!")

def avatar2():#describes avatar 2
    print("Avatar 2") 
    print("They are a very quiet person. They love to keep to themsleves and have alone time daily. They would rather spend time reading than going out with friends!")   

def avatar3():#describes avatar 3
    print("Avatar 3")
    print("They are a very adventurous person. They love to explore and discover new things about the nature around them.")

def yesno():#asks the user if they are sure if they will continue with the avatar they chose
    print("Are you sure you would want to stay with your choice of avatar?")
    answer = input("Please type either yes or no: ")
    if answer == "yes":
        pregame() 
    elif answer == "no": 
        customizing2()
    else:
        print() 
        print()
        print("That input you entered is not apart of the choices.")
        print("Please choose either yes or no")  
        yesno()  

def customizing1(): #leads to the choices of what avatars are there
    print()
    print()
    print()
    print()
    print("Welcome to the Customizing Station!")
    print("In here, we will customize your very own character, by choosing which avatar your would like to be.")
    print("Choose the avatar you would like to be or relate to the most.")

def customizing2(): #allows the user to enter which character they would like by entering the numbr that coressponds with the avatar  
    print()
    print()
    avatar1()
    print()
    avatar2()
    print()
    avatar3()
    print()
    print("What is your choice?")
    print("1) Avatar 1")
    print("2) Avatar 2")
    print("3) Avatar 3")
    numbers = int(input("Enter the number for the avatar your would like: "))
    print()
    print()
    if numbers == 1:
        print("You chose Avatar 1: You chose the avatar that is very outgoing and loves to hangout with other! ")
        yesno() 
    elif numbers == 2: 
        print("You chose Avatar 2: You chose the avatar that is a quiet type of person and loves to have alone time!")
        yesno()
    elif numbers == 3:
        print("You chose Avatar 3: You chose the avatar that is very adventurous and loves to explore the things around them!") 
        yesno()
    else:
        print("That number you chose is not apart of the choices.")
        print("Please choose a number between 1 to 3")  
        customizing2() 

def pregame(): #builds up to the game.Tells the user what happens and why they end up on a island stranded
    print()
    print()
    print()
    print()
    print("OK! Let's Begin!")
    print("Once upon a time,", name,"traveled everywhere!")
    print(name," went on trips where no one dared to go!")
    print("One day,", name,"boarded a ship to go to an exotic place.")
    print("However, this did not end well.")
    print("The ship collided with rocks and sunk!")
    print("Everyone else sunk and were never found again!")
    print("But", name,"survived!")
    print("You got washed up on an island!")
    print("You are all alone and no one else is there to help!")

def basicinstructions():#this tells the user about how many lives they have and wishes them good luck
    print()
    print() 
    print()
    print()
    print("Here are the instructions on how to survive!")
    print()
    print("You have infinite lives")
    print("But you will start with 3 lives.")
    print("Every decision you make is important!")  
    print("GOOD LUCK!")
    print()
    print() 

def game1():#shows the time passing and sets up the game to go on to the food function
    for x in range(1,6):
        print("        Hour",x,"🕒")
        print()
    print("You have been on the island for about 5 hours now!")
    print("You are starting to get hungry")
    option1(hearts)


hearts = 3 # this is how many hearts the user starts with, but they have infinite lives.
def option1(hearts):#asks the user what they would want to do, and if they choose the wrong choice, they will lose a hearts
    print("What do you want to do?")
    print("1) Start looking for food")
    print("2) Lay there and cry")
    print("3) Throw a tantrum")
    options = int(input("Enter the number for the option you would like to do: "))
    print()
    print()
    if options == 1: 
        food(hearts)
    elif options == 2:
        print("You lost 1 heart")
        hearts -= 1 
        print ("You have " + str(hearts) + " hearts remaining.")
        option1(hearts)
    elif options == 3:
        print("You lost 1 heart")
        hearts -= 1
        print ("You have " + str(hearts) + " hearts remaining.")
        option1(hearts)
    else:
        print("That number you chose is not apart of the choices.")
        print("Please choose a number between 1 to 3")  
        option1(hearts)
        

def food(hearts):#In this function, it tells the user that they are going to get food, but they need to do specific things in order to get the food
    print ("You have " + str(hearts) + " hearts remaining.")
    print("You now get sticks to create an ax to obtain your food.")
    print("Please save some wood for future usage like creating a fire.")
    print()
    count = 0
    while count<=30:
        print(count,"minutes")
        count = count + 5 
    else:
      print()
      print("After " +str(count),"minutes, you are finished gathering your sticks to create an ax to cut the vegetation.")
      print("You have now gathered your vegetables to eat.")
      option2(hearts)

def option2(hearts): #asks the user what they would want to do, and if they choose the wrong choice, they will lose a hearts 
    print("What do you want to do?")
    print("1) Go to the river to wash vegetables")
    print("2) Just eat it raw")
    options = int(input("Enter the number for the option you would like to do: "))
    print()
    print()
    if options == 1: 
        river(hearts)
    elif options == 2:
        print("You lost 1 heart")
        hearts -= 1 
        print ("You have " + str(hearts) + " hearts remaining.")
        option2(hearts)
    else:
        print("That number you chose is not apart of the choices.")
        print("Please choose a number between 1 to 3")  
        option2(hearts)  

def river(hearts):#tells the user how many hearts they have left and that they are going to a river to cleanse the vegetables
    print ("You have " + str(hearts) + " hearts remaining.")
    print("You now are going to the river.")
    print("You are going to cleanse the vegetables.")
    print()
    for x in range(1,6):
        print("        Hour",x,"🕒")
        print()
    option3(hearts)

def option3(hearts): #asks the user what they would want to do, and if they choose the wrong choice, they will lose a hearts
    print("After cleaning the vegetables...")   
    print("What do you want to do?")
    print("1) Just eat it raw")
    print("2) Go and cook the vegetable first")
    options = int(input("Enter the number for the option you would like to do: "))
    print()
    print()
    if options == 1: 
        print("You lost 1 heart")
        hearts -= 1 
        print ("You have " + str(hearts) + " hearts remaining.")
        option3(hearts)
    elif options == 2:
        fire(hearts)
    else:
        print("That number you chose is not apart of the choices.")
        print("Please choose a number between 1 to 3")  
        option3(hearts)     

def fire(hearts):#The user is then going to use the sticke they have collected to create a fire to cook the vegetables
    print("You now will use the saved sticks!")
    print("You will now create a fire to cook the vegetables")
    print()
    option4(hearts)

def option4(hearts):#asks the user what they would want to do, and if they choose the wrong choice, they will lose a hearts
    print("What do you do?")
    print("1) Sit there and watch the fire")
    print("2) Cook the food and eat")
    options = int(input("Enter the number for the option you would like to do: "))
    print()
    print()
    if options == 1: 
        print("You lost 1 heart")
        hearts -= 1 
        print ("You have " + str(hearts) + " hearts remaining.")
        option4(hearts)
    elif options == 2:
        shelter(hearts)
    else:
        print("That number you chose is not apart of the choices.")
        print("Please choose a number between 1 to 3")  
        option4(hearts)    

def shelter(hearts):#The user needs to build a house for their shelter
     print("You will now need to build a house.")
     print("You must get some wood for the house.")  
     wood(hearts)      

def wood(hearts):#the user has finished chopping all the wood and the program shows that 3 hours have passed
    print("Chop, chop, chop") 
    for x in range(1,3):
        print("        Hour",x,"🕒")
        print()
    print("After 3 hours, you have finished chopping and collecting all the wood you need.")
    food2(hearts)

def food2(hearts):#In this function, it tells the user that they are going to get food, but they need to do specific things in order to get the food
    print ("You have " + str(hearts) + " hearts remaining.")
    print("You now get sticks to create an ax to obtain your food.")
    print("Please save some wood for future usage like creating a fire.")
    print()
    count = 0
    while count<=30:
        print(count,"minutes")
        count = count + 5 
    else:
      print()
      print("After " +str(count),"minutes, you are finished gathering your sticks to create an ax to cut the vegetation.")
      print("You have now gathered your vegetables to eat.")
      option5(hearts)

def option5(hearts):#asks the user what they would want to do, and if they choose the wrong choice, they will lose a hearts
    print("What do you want to do?")
    print("1) Go to the river to wash vegetables")
    print("2) Just eat it raw")
    options = int(input("Enter the number for the option you would like to do: "))
    print()
    print()
    if options == 1: 
        river2(hearts)
    elif options == 2:
        print("You lost 1 heart")
        hearts -= 1 
        print ("You have " + str(hearts) + " hearts remaining.")
        option5(hearts)
    else:
        print("That number you chose is not apart of the choices.")
        print("Please choose a number between 1 to 3")  
        option5(hearts)  

def river2(hearts):#shows how many hearts the user has and the user now goes to the river to wash the vegetables, and shows that 6 hours have passed
    print ("You have " + str(hearts) + " hearts remaining.")
    print("You now are going to the river.")
    print("You are going to cleanse the vegetables.")
    print()
    for x in range(1,6):
        print("        Hour",x,"🕒")
        print()
    option6(hearts)

def option6(hearts):#asks the user what they would want to do, and if they choose the wrong choice, they will lose a hearts
    print("After cleaning the vegetables...")   
    print("What do you want to do?")
    print("1) Just eat it raw")
    print("2) Go and cook the vegetable first")
    options = int(input("Enter the number for the option you would like to do: "))
    print()
    print()
    if options == 1: 
        print("You lost 1 heart")
        hearts -= 1 
        print ("You have " + str(hearts) + " hearts remaining.")
        option3(hearts)
    elif options == 2:
        fire2(hearts)
    else:
        print("That number you chose is not apart of the choices.")
        print("Please choose a number between 1 to 3")  
        option3(hearts)     

def fire2(hearts):#he user is then going to use the sticke they have collected to create a fire to cook the vegetables
    print("You now will use the saved sticks!")
    print("You will now create a fire to cook the vegetables")
    print()
    option7(hearts)

def option7(hearts):#asks the user what they would want to do, and if they choose the wrong choice, they will lose a hearts
    print("What do you do?")
    print("1) Sit there and watch the fire")
    print("2) Cook the food and eat")
    options = int(input("Enter the number for the option you would like to do: "))
    print()
    print()
    if options == 1: 
        print("You lost 1 heart")
        hearts -= 1 
        print ("You have " + str(hearts) + " hearts remaining.")
        option7(hearts)
    elif options == 2:
        finishgame(hearts)
    else:
        print("That number you chose is not apart of the choices.")
        print("Please choose a number between 1 to 3")  
        option7(hearts)    

def finishgame(hearts): #the user has finished eating and they continue to build the house. After 3 hours, they finish and then the game ends
#The program prints the score/hearts the user has and they user can then compare the number of hearts they have with others who played the game before.     
     print("You have now eaten and are ready to continuue.")
     print("You are now building your house.")    
     for x in range(1,3):
        print("        Hour",x,"🕒")
        print()
     print("After 3 hours, you have finished your house!")
     print()
     print()
     print()
     print("THIS IS YOUR SCORE!")
     print ("You have " + str(hearts) + " hearts remaining.")
     print("You can compare your score with others outside of the game")
     print("Thank you for playing!")





#calls the functions to start the game
welcome() 
customizing1()
customizing2()
basicinstructions()
game1()
