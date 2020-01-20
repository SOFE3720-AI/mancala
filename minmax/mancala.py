#!/usr/bin/python

"""
Example of input:

1
0
4 4 4 4 4 4
0
4 4 4 4 4 4

"""

class MancalaBoard():

    def __init__(self,player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
        self.player = player
        #setting the board in player's perspective
        if self.player == 1:    # if player is player1
            self.playerMancala = player1Mancala
            self.playerMarbles = player1Marbles
            self.opponentMancala = player2Mancala
            self.opponentMarbles = player2Marbles
        else:                   # if player is player2
            self.playerMancala = player2Mancala
            self.playerMarbles = player2Marbles
            self.opponentMancala = player1Mancala
            self.opponentMarbles = player1Marbles
            

     
def nextBoard(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles, slot):
    slot = slot - 1 
    if player == 1:
        playerMancala = player1Mancala
        playerMarbles = player1Marbles
        opponentMancala = player2Mancala
        opponentMarbles = player2Marbles
    else:
        playerMancala = player2Mancala
        playerMarbles = player2Marbles
        opponentMancala = player1Mancala
        opponentMarbles = player1Marbles

    marbleSlot = playerMarbles[slot]
    playerMarbles[slot] = 0
    
    
    


    print("---Currrent State --- ")
    print(player)
    print("Available marbles: {}".format(marbleSlot))
    print(playerMancala)
    print(playerMarbles)
    print(opponentMancala)
    print(opponentMarbles)

def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
    nextBoard(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles, 5)


player = int(input())
mancala1 = int(input())
mancala1_marbles = [int(i) for i in input().strip().split()]
mancala2 = int(input())
mancala2_marbles = [int(i) for i in input().strip().split()]
printNextMove(player, mancala1, mancala1_marbles, mancala2, mancala2_marbles)