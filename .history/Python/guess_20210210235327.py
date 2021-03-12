import random
import time
players = []
punishments = []
while True:
    player = input('name\n')
    if player == '': break
    players.append(player)
    # punishment = input('your punishment?\n')
    # if punishment != '':
    #     punishments.append(punishment)
    # time.sleep(0.5)
min = int(input("\n\n\n\n\nMinimum number?\n"))
max = int(input("Maximum number?\n"))
ran = int((random.random() * (max - min + 1)) + min)
guesses = []
if len(players) == 1
    print("Your guess:")
status = True
while status:

    for i in players:
        time.sleep(0.5)
        if len(players) != 1: inp = int(input('It\'s ' + i + '\'s turn\n'))
        else: inp = int(input())
        guesses.append(inp)
        if inp < ran:
            print("too small")
        elif inp > ran:
            print("too large")
        else:   
            if len(players) == 1:
                print(i + " wins")
                print(int((1/len(guesses)) * 100),"%")
            # if len(punishments) != 0:
            #     rand = int(random.random() * len(punishment))
            #     print(rand)
            #     if rand >= len(punishments):
            #         rand -= 1
            #     print(i + '\'s punishment: ' + punishments[rand])
            status = False
            break

    