#!/usr/bin/python

"""
Example of input:

1
0
4 0 0 0 2 4
0
4 4 4 4 4 4

"""
#TODO: findNextMoves

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
        for i in range(1,7):
            if self.playerMarbles[i-1]>0:
                nextBoard(self,i,False)
            

    #print current state of the board
    def printBoard(self):
        print("---Current State ---")
        print("player: {}".format(self.player))
        print(self.playerMancala)
        print(self.playerMarbles)
        print(self.opponentMancala)
        print(self.opponentMarbles)

def nextBoard(MancalaBoard,slot,repeat):
    # chosen slot must not be empty
    repeat = False
    player = MancalaBoard.player
    playerMancala = MancalaBoard.playerMancala
    playerMarbles = MancalaBoard.playerMarbles.copy()
    opponentMancala = MancalaBoard.opponentMancala
    opponentMarbles = MancalaBoard.opponentMarbles.copy()

    # grabbing marble from designated slot
    slotMarbles = MancalaBoard.playerMarbles[slot-1]
    playerMarbles[slot-1] = 0

    boardArray = []
    boardArray.extend(playerMarbles)
    boardArray.append(playerMancala)
    boardArray.extend(opponentMarbles)

    nextSlot = slot
    while slotMarbles > 0:
        nextboardSlot = nextSlot % 13
        slotMarbles -= 1
        boardArray[nextboardSlot] += 1
        nextSlot += 1

        # steal function
        if slotMarbles == 0 and nextboardSlot < 6: 
            if boardArray[nextboardSlot] == 1:
                stealingScore = boardArray[nextboardSlot+7]
                boardArray[nextboardSlot+7] = 0
                boardArray[6] += stealingScore

    
    
    playerMarbles = boardArray[0:6]
    playerMancala = boardArray[6]
    opponentMarbles = boardArray[7:13]

    if (nextSlot-1) == 6:
        repeat = True
    
    if repeat == False: 
        if player == 1:
            boardResult = MancalaBoard(1,playerMancala, playerMarbles, opponentMancala, opponentMarbles)
        else:
            boardResult = MancalaBoard(2,opponentMancala, opponentMarbles, playerMancala, playerMarbles)
    
        
    print("---state of next board --- ")
    print("slot selected: {}".format(slot))

    print(player)
    print(playerMancala)
    print(playerMarbles)
    print(opponentMancala)
    print(opponentMarbles)
    print("Repeat: {}".format(repeat))



def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
    board1 = MancalaBoard(player,player1Mancala, player1Marbles, player2Mancala, player2Marbles)
    board1.findNextMoves()
    

player = int(input())
mancala1 = int(input())
mancala1_marbles = [int(i) for i in input().strip().split()]
mancala2 = int(input())
mancala2_marbles = [int(i) for i in input().strip().split()]
printNextMove(player, mancala1, mancala1_marbles, mancala2, mancala2_marbles)