import random

print('The rules are :\n' 
+ "Rock vs Paper ... Paper wins \n"
+ "Rock vs scissors...Rock wins \n"
+ "Paper vs Scissors... Scissors wins \n")

while True:
    print ("Please enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("Enter your choice:"))

    while choice > 3 or choice < 1: 
        choice = int(imput("Please Enter a valid choice"))
    if choice == 1:
            choice_name = 'Rock'
    elif choice == 2:
            choice_name = 'Paper'
    else:
            choice_name = 'scissors'

         
    print('Your choice is \n', choice_name)
    print('Computers Turn....')


