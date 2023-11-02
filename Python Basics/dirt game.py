name = input("type your name: ")


print("welcome", name, "to dir road adventure")


answer =input("you are on a dirt road, it has come to an end and you can go left and rught and what way would you like to go (left/right): ").lower()

if answer  == "left":
    answer = input("you come to ariver and you can walk around it or swim accross? type walk to walk and swim to swim: ")
    
    if answer == "swim":
        print("you swim accross and wee eaten by elegator!")

    elif answer == "walk":
        print("you walked for many miles ran out of water and you lost the game!")

    else:
        print("not a valid option. you lose!")

elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("you go back and you lose")

    elif answer == "cross":
        answer =input("you crossed the bridge and meet a stranger, do you talk to them (yes/no)?: ")
        if answer=="yes":
            print("you talk to the stranger, and they give you gold. you win!")

        elif answer == "no":
            print("you ignored the stranger and they are offended. you lose!")
        
        else:
            print("not a valid option. you lose!")
        


else:
    print("not a valid option. you lose!")

print("thanks for trying", name)





    
    
