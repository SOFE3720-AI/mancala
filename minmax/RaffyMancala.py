
def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
    if player == '1':
        marbles = player1Marbles
        score = player1Mancala
        enemyMarbles = player2Marbles
        enemyScore = player2Mancala
    elif player == '2':
        marbles = player2Marbles
        score = player2Mancala
        enemyMarbles = player1Marbles
        enemyScore = player1Mancala
    
    board = createBoard(marbles, score, enemyMarbles, enemyScore)
    select = minimax(board, True, 8, -10000, 10000)

    print(select[1])

# Creates the Mancala board
def createBoard(marbles, score, enemyMarbles, enemyScore):
    board = []
    for x in marbles:
        board.append(x)
    
    board.append(int(score))

    for x in enemyMarbles:
        board.append(x)

    board.append(int(enemyScore))

    return board

# Gets score of a move
def getScore(board, end, depth):
    if sum(board[:7]) > sum(board[7:]) and end:
        score = 100 + depth
    elif sum(board[:7]) < sum(board[7:]) and end:
        score = -100 - depth
    else:
        score = (board[6] - board[13])*2 + (sum(board[:7]) - sum(board[7:]))
    
    return score
    # Find better way to score moves and add how many turns to win
    #score = (sum(board[:7]) - sum(board[7:]))
    #score = board[6] - board[13]

# Minimax algorithm: Checks for all possible cases then find highest score achievable
def minimax(board, maxPlayer, depth, alpha, beta):
    end = checkGameStatus(board)
    if depth == 0 or end:
        score = getScore(board, end, depth)

        return score, None

    if maxPlayer:
        bestScore = -100000000
        move = None
        # Calls minimax on all 6 possible moves
        for i in range(6):
            if board[i] != 0:
                # Finds next state when that move is chosen
                futureBoard = getFutureState(i+1, board.copy(), maxPlayer)  
                # checks if bot gets an extra turn
                if futureBoard[1]:
                    # Has to add score when it gets an extra turn
                    score = minimax(futureBoard[0], futureBoard[1], depth , alpha, beta)
                else:
                    score = minimax(futureBoard[0], futureBoard[1], depth - 1, alpha, beta)               

                if score[0] > bestScore:     
                    bestScore = score[0]
                    move = i+1

                alpha = max(alpha, bestScore)
                # Alpha beta pruning
                if beta <= alpha:
                    break

        return bestScore, move

    else:
        bestScore = 10000000
        move = None
        # Calls minimax on all 6 possible moves
        for i in range(6):
            if board[i+7] != 0:
                # Finds next state when that move is chosen
                futureBoard = getFutureState(i+8, board.copy(), maxPlayer)
                 # checks if bot gets an extra turn
                if futureBoard[1] == False:
                    score = minimax(futureBoard[0], futureBoard[1], depth, alpha, beta ) 
                else:
                    score = minimax(futureBoard[0], futureBoard[1], depth - 1, alpha, beta)               

                if score[0] < bestScore:     
                    bestScore = score[0]
                    move = i+8
                beta = min(beta, bestScore)
                # Alpha beta pruning
                if beta <= alpha:
                    break
        return bestScore, move


# Gets the future state of the board
def getFutureState(select, board, maxPlayer):
    moves = board[select - 1]
    board[select - 1] = 0
    i = select

    # Default value of extra
    if maxPlayer:
        extra = False
    else:
        extra = True
    
    while moves > 0:
        if i >= len(board):
            i = 0
        # Stealing
        if moves == 1 and board[i] == 0 and i != 6 and i != 13:
            board[i] = board[12-i]
            board[12-i] = 0
        
        # Extra turn
        if moves == 1:
            if maxPlayer and i == 6:
                extra = True 
            elif maxPlayer == False and i == 13:
                extra = False

        board[i]+=1
        i+=1
        moves-=1
   
    return board, extra

#check if you won or lose
def checkGameStatus(board):
    if sum(board[:6]) == 0 or  sum(board[7:13]) == 0:
        return True
    else:
        return False



def main():
    player = input()
    mancala1 = input()
    mancala1_marbles = [int(i) for i in input().strip().split()]
    mancala2 = input()
    mancala2_marbles = [int(i) for i in input().strip().split()]
    printNextMove(player, mancala1, mancala1_marbles, mancala2, mancala2_marbles)

main()
