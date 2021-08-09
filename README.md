# Basic elo rating system based on the chess rating system.
https://en.wikipedia.org/wiki/Elo_rating_system

## How it works
Generates a specific amount of players which then plays out all the games against all the possible players.
Each players initial score is generated using a normal distribution with a mean of 1000 and a variance of 500.
Once after each game, the score of both players are updated. The K factor also gets adjust based on the amount of games the player has played. 


Progress of a player over time
<img width="644" alt="Screenshot 2021-08-09 at 1 56 53 PM" src="https://user-images.githubusercontent.com/40253263/128702579-9444d9d2-071c-4df5-907d-738b605a7007.png">



TODO:
dynamically adjust K factor: ie, if a low elo player suddenly beats a much higher elo player, the K factor should be readjusted.
