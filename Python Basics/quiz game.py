print("welcome to my computer quiz!")

playing = input("do you wanna play? ")

if playing != 'yes':
    print("as you wish :)")
    quit()

print("okay! lets play")

score = 0


answer = input("what does cpu means? ")
if answer == "central processing unit":
    print('correct')
    score += 1
else:
    print('incorrect')


answer = input("what does gpu means? ")
if answer == "graphic processing unit":
    print('correct')
    score += 1
else:
    print('incorrect')



answer = input("what does ram means? ")
if answer == "random access memory":
    print('correct')
    score += 1
else:
    print('incorrect')

print("you got " + str(score) + " score")
print("thanks for playing!")

