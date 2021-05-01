'''Following are the rules of the game:
Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water.
Gun vs. Snake: Gun will kill the snake and win.'''


import random


def swg(you, comp):
    if(comp == you):
        return 0
    if(comp == 's' and you == 'g'):
        return -1
    elif(comp == 's' and you == 'w'):
        return 1
    if(comp == 'g' and you == 'w'):
        return 1
    elif(comp == 'g' and you == 's'):
        return -1
    if(comp == 'w' and you == 'g'):
        return -1
    elif(comp == 'w' and you == 's'):
        return 1


n = random.randrange(1, 101, 1)
you = input("enter 'g' for gun 'w' for water 's' for snake:")
if(n < 33):
    comp = 'g'
elif(n > 33 and n < 66):
    comp = 's'
else:
    comp = 'w'
print("comp choose ", comp, " you choose", you)
result = swg(you, comp)
if(result == 0):
    print("math draw!!!!")
elif(result == -1):
    print("you loose!!!!!!")
else:
    print("you won!!!!!!!")
