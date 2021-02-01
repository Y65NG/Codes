import time
import random
class Player:
    actions = []
    def __init__(self,name,hp,atk,df):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.df = df
        self.action = ''
        self.obj = ''
        self.point = 0


    def attack(self,other):
        
        if self.atk > other.df:
            other.hp -= self.atk - other.df
            other.df -= 1
            
        else:
            other.df -= self.atk
            
            
        if other.hp > 0:    
            print(other.name + ':')
            print('防御: ' + str(other.df))
            print('血量: ' + str(other.hp))    



players = {}
num = int(input('number of players?\n'))
for a in range(num):
    name = input('name?\n')
    hp = float(input('血量?\n'))
    atk = float(input('攻击?\n'))
    df = float(input('防御?\n'))
    
    players[name] = Player(name,hp,atk,df)

time.sleep(0.7)
print('开始游戏')
print('_____________________________________')
time.sleep(0.7)
print('''tips:
point - 1
attack - 2
defend - 3
''')
time.sleep(1)

while True:
    for turn in players:
        time.sleep(1)
        action = input('It\'s %s\'s turn \n' %(turn))
        if action == '2':
            obj = input('->')
            players[turn].obj = obj
        
        players[turn].action = action
        
        
    for turn in players:
        this = players[turn]
        obj = players[turn].obj
        time.sleep(1)
        
        if this.action == '2':
           
            print(this.name + ' attacks ' + obj)
            if players[obj].action != '3':
                
                players[obj].hp -= this.atk - players[obj].df * 0.5
                if players[obj].df != 0: players[obj].df -= 1
                    
                if players[obj].hp > 0:    
                    print(players[obj].name)
                    print('点数: ' + str(players[obj].point))
                    print('防御: ' + str(players[obj].df))
                    print('血量: ' + str(players[obj].hp))
                    print('\n')
                else:
                    print(players[obj].name + '的血量: 0')
                    print(players[obj].name + ' dies')
                    del players[obj]
                    break
            else:
                if players[obj].df > 0:
                    players[obj].df -= 1
                else:
                    players[obj].hp -= 1
                    if players[obj].op == 0:
                        print(players[obj].name + '的血量: 0')
                        print(players[obj].name + ' dies')
                        del players[obj]
                        break
                        
                print(players[obj].name)
                print('点数: ' + str(players[obj].point))
                print('防御: ' + str(players[obj].df))
                print('血量: ' + str(players[obj].hp))
                print('\n')
        if this.action == '1':
            this.point += 1 
            print(this.name + ' gets 1 point')
            print(this.name)
            print('点数: ' + str(this.point))
            print('防御: ' + str(this.df))
            print('血量: ' + str(this.hp))
            print('\n')

            
            
            
            
        

