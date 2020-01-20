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
        self.nextpossible = []
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
    
    def findNextMoves(self):
        # function to populate nextpossible 
        pass

    #print current state of the board
    def printBoard(self):
        print("---Current State ---")
        print("player: {}".format(self.player))
        print(self.playerMancala)
        print(self.playerMarbles)
        print(self.opponentMancala)
        print(self.opponentMarbles)

def nextBoard(MancalaBoard,slot):
    player = MancalaBoard.player
    playerMancala = MancalaBoard.playerMancala
    playerMarbles = MancalaBoard.playerMarbles
    opponentMancala = MancalaBoard.opponentMancala
    opponentMarbles = MancalaBoard.opponentMarbles
    
    # grabbing marble from designated slot
    slotMarbles = MancalaBoard.playerMarbles[slot-1]
    playerMarbles[slot-1] = 0

    
    # distributing marbles
    nextSlot = slot
    while slotMarbles > 0:
        

    print("---state of next board --- ")
    print("slot selected: {}".format(slot))
    print("Marbles found in slot: {}".format(slotMarbles))

    print(player)
    print(playerMancala)
    print(playerMarbles)
    print(opponentMancala)
    print(opponentMarbles)



def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
    board1 = MancalaBoard(player,player1Mancala, player1Marbles, player2Mancala, player2Marbles)
    nextBoard(board1,4)

player = int(input())
mancala1 = int(input())
mancala1_marbles = [int(i) for i in input().strip().split()]
mancala2 = int(input())
mancala2_marbles = [int(i) for i in input().strip().split()]
printNextMove(player, mancala1, mancala1_marbles, mancala2, mancala2_marbles)