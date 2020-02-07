
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
    turn1 = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
    turn2 = [4,4,0,5,5,5,1,4,4,4,4,4,4,0]
    turn3 = [5,0,6,6,5,5,1,4,4,0,5,5,0,2]
   
    
    # Ideal turn1 moves
    if board == turn1:
        print(3)
    elif board == turn2:
        print(6)
    elif board == turn3:
        print(1)
    else:
        # To find move count
        moves = findMoves(board, True)
        depth = 8
        # Iterative deepening
        if (sum(board[:6]) + sum(board[7:13])) < 12:
            depth +=5
        elif (sum(board[:6]) + sum(board[7:13])) < 18:
            depth +=4
        elif (sum(board[:6]) + sum(board[7:13])) < 20:
            depth +=3
        elif ((sum(board[:6]) + sum(board[7:13])) < 23) and len(moves) < 5:
            depth +=2
        elif (sum(board[:6]) + sum(board[7:13])) < 23:
            depth +=1
        elif ((sum(board[:6]) + sum(board[7:13])) < 30) and len(moves) < 5:
            depth +=1


        select = minimax(board, True, depth, -10000, 10000)
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


# Possible Heuristic
# (sum(board[:7]) - sum(board[7:])) -> # of your marble - enemy marble (including mancala)
# board[6] - board[13] -> your mancala - enemy mancala
# (24 - board[13]) -> how far enemy is close to winning
# (board[6]-24) -> how close you are to winning
# board[5] -> # of marbles in 6th hole (i see the top two guys always storing in 6th hole)
# board[3] -> # of marbles in 4th hole (usually a good hole to store marbles)
# (sum(board[:6]) - sum(board[7:13])) -> # of your marble - enemy marble (not including mancala; usually performs worst) 

# Gets score of a move
def getScore(board, end, depth,maxPlayer):
    if (sum(board[:7]) > sum(board[7:]) and end) or board[6] > 24:
        score = 1000 + depth
    elif (sum(board[:7]) < sum(board[7:]) and end) or board[13] > 24:
        score = -1000 - depth
    else:
        score = (board[6] - board[13])*3 + (sum(board[:7]) - sum(board[7:]))

            
    return score

# Find possible moves from a given board state
def findMoves(board, maxPlayer):
    moves = []
    for i in range(6):
        if maxPlayer:
            if board[i] != 0:
                moves.append(i)
        else:
            if board[i+7] != 0:
                moves.append(i)

    return moves



# Minimax algorithm: Checks for all possible cases then find highest score achievable
def minimax(board, maxPlayer, depth, alpha, beta):
    end = checkGameStatus(board)
    if depth == 0 or end:
        score = getScore(board, end, depth,maxPlayer)

        return score, None

    # Find possible moves from the board state
    moves = findMoves(board,maxPlayer)

    if maxPlayer:
        bestScore = -100000000
        move = None
        # Calls minimax on all 6 possible moves
        for i in moves:
            # Finds next state when a move is chosen
            futureBoard = getFutureState(i+1, board.copy(), maxPlayer)  

            # checks if bot gets an extra turn
            if futureBoard[1]:
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
        for i in moves:
 
            # Finds next state when a move is chosen
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
