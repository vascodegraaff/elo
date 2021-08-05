import numpy as np
import random
import matplotlib.pyplot as plt
import uuid

class Player:
    #initializes a random players with a random elo using a normal distribution N(1000,500)
    def __init__(self):
        self.id = str(uuid.uuid4())[:8]
        self.rating = np.random.normal(1000,300) 
        self.games = []
        self.k = 32
    def __str__(self):
        return "Player: " + self.id + ", elo: " + str(round(self.rating)) + ", Games: " + str(len(self.games))

    def update(self, rating):
        self.rating = rating


class Game:
    def __init__(self, p1, p2, res):
        self.p1 = p1
        self.p2 = p2
        self.res = res

    def __str__(self):
        if(res):
            return p1 + " won"
        else:
            return p2 + " won"
#r1 & r2 are ratings of each player, res is the result, 1 means r1 wins, 0 means r2 wins
def calc(p1, p2, res):
    if p1 == p2:
        return
    #estimation of player 1 and player 2 winning
    e1 = 1/(1+pow(10,((p2.rating -p1.rating)/400)))
    e2 = 1/(1+pow(10,((p1.rating-p2.rating)/400)))

    if(res):
        p1.update(p1.rating + p1.k * (1 - e1))
        p2.update(p2.rating + p2.k * (0 - e2))
    else:
        p1.update(p1.rating + p1.k * (0 - e1))
        p2.update(p2.rating + p2.k * (1 - e2))

    game = Game(p1,p2,res)
    p1.games.append(game)
    p2.games.append(game)
    

def main():
    players = []
    [players.append(Player()) for i in range(20)]
    
    # https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
    
    for i in range(len(players)):
        for j in range(len(players)-1):
            calc(players[i], players[j], bool(random.getrandbits(1)))
            print(players[i])
#            print(players[j])




if __name__ == "__main__":
    main()




