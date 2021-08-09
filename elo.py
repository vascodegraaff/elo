import numpy as np
import random
import matplotlib.pyplot as plt
import uuid
from itertools import combinations

class State:
    def __init__(self):
        self.players = []
        [self.players.append(Player()) for i in range(100)]
        for i, j in combinations(self.players, 2):
            calc(i, j)
            print(i)
            print(j)

    def update(self):
        self.players.sort(key=lambda x: x.rating, reverse=False)



    def find(self, id):
        for i in self.players:
            if i.id == id:
                return i

class Player:
    # initializes a random players with a random elo using a normal distribution N(1000,500)
    def __init__(self):
        self.id = str(uuid.uuid4())[:8]
        self.rating = np.random.normal(1000, 500)
        self.games = []
        self.k = 32

    def __str__(self):
        # return "Player: " + self.id + ", elo: " + str(round(self.rating)) + ", Games: " + str(len(self.games))
        return str(self.id) + ": " + str(round(self.rating))

    def __repr__(self):
        return self.__str__()

    def update(self, rating):
        self.rating = rating



# The game object gets stored inside the player object, p1 is the player, p2 is the opponent, res is whether or not p1 wins, rating is p1's new rating 
class Game:
    def __init__(self, id, p1, p2, res, rating):
        self.id = id
        self.p1 = p1
        self.p2 = p2
        self.res = res
        self.rating = rating

    def __str__(self):
        return "id: " + str(self.id) + ", " + str(self.p1.id) if self.res else str(self.p2.id) + " wins, new rating: " + str(self.rating)
    def __repr__(self): 
        return self.__str__()

def calc(p1, p2):
    if p1 == p2:
        return
    # estimation of player 1 and player 2 winning
    e1 = 1/(1+pow(10, ((p2.rating - p1.rating)/400)))
    e2 = 1/(1+pow(10, ((p1.rating-p2.rating)/400)))

    res = random.random() < e1
   # p1 wins
    if(res):
        p1.update(p1.rating + p1.k * (1 - e1))
        p2.update(p2.rating + p2.k * (0 - e2))
    # p2 wins
    else:
        p1.update(p1.rating + p1.k * (0 - e1))
        p2.update(p2.rating + p2.k * (1 - e2))

    # this might be a bad solution since we initialize the game twice and just copy the id.
    id = str(uuid.uuid4())[:8]
    p1.games.append(Game(id, p1,p2,res, p1.rating))
    p2.games.append(Game(id, p2,p1,not res, p2.rating))


def main():
    state = State()
    state.update()

    progress = [i.rating for i in state.players[50].games]
    n = [i for i in range(len(progress))]
    plt.plot(n, progress)
    plt.show()

if __name__ == "__main__":
    main()
