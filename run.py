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
    """
    computer chooses randomly any number among 1,2 amd 3
    using randint method
    """
    comp_choice = random.randint(1,3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            comp_choice_name = 'Rock'

        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        
        else:
            comp_choice_name = 'Scissors'

        print("Computers choice is \n", comp_choice_name)
        print(choice_name, "vs", comp_choice_name)




