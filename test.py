# choose integer number
just_price = 670
# user number
user_price = 0

# while price is not egal to just price plays loop
while just_price != user_price:
    # user price must be an integer
    user_price = int(input("Entrer un prix:"))
    # if user number is bigger than winner number
    if user_price > just_price:
        # display : it's less!
        print("C'est moins!")
    # else if user number is smaller than winner number
    elif user_price <670:
        # display : it's bigger!
        print("C'est plus!")
    # else display : you win!
    else:
        print("Tu as gagné!")
        # end process
        break