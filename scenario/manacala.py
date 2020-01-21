
def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
    if player == '1':
        marbles = player1Marbles
        score = player1Mancala
        enemyMarbles = player2Marbles
    elif player == '2':
        marbles = player2Marbles
        score = player2Mancala
        enemyMarbles = player1Marbles
        
    extra = extraTurnCheck(marbles)
    avoid = avoidSteal(marbles, enemyMarbles)
    
    if extra != -1:
        print(extra)
    elif avoid != -1:
        print(avoid)
    else:
        # Select rightmost hole that is not empty   
        for i in reversed(range(6)):
            if marbles[i] != 0:
                select = i+1
                break
        print(select)

        
# Checks if its possible to get an extra turn
# Checks from right to left how many marbles in the hole
def extraTurnCheck(marbles):
    j=1
    for i in reversed(range(6)):
        if marbles[i] == j:
            return i+1
        j+=1

    return -1

def avoidSteal(myMarbles, enemyMarbles):
    # looks for an empty hole in opponents board
    for i in reversed(range(5)):
        if enemyMarbles[5-i] == 0 and myMarbles[i] >= 4:
            j=1
            # Check to the left of the hole 
            for x in reversed(range(5-i)):
                if enemyMarbles[x] == j:
                    return i+1
                j+=1
    return -1

def main():
    player = input()
    mancala1 = input()
    mancala1_marbles = [int(i) for i in input().strip().split()]
    mancala2 = input()
    mancala2_marbles = [int(i) for i in input().strip().split()]
    printNextMove(player, mancala1, mancala1_marbles, mancala2, mancala2_marbles)

main()
