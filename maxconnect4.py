#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

#Kunal Samant
#1001534662

import sys
from maxConnect4Game import *

def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    currentGame.aiPlay() 

    print('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame, arg, computer_file, human_file):
    # Fill me in
    if arg == 'human-next':
        while(currentGame.pieceCount != 42):
            entry = -1

            while (entry < 1 or entry > 7) or (currentGame.gameBoard[0][entry-1] != 0):
                try:
                    entry = int(input("Choose a move (1-7): "))
                except:
                    entry = -1
                    print('Between 1 and 7...')
            
            currentGame.playPiece(entry-1)

            try:
                currentGame.gameFile = open(human_file, 'w')
            except:
                sys.exit('Error opening output file.')

            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()

            if currentGame.currentTurn == 1:
                currentGame.currentTurn = 2
            elif currentGame.currentTurn == 2:
                currentGame.currentTurn = 1

            print('Game state after move:')
            currentGame.printGameBoard()
            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            if currentGame.pieceCount == 42:
                print('BOARD FULL\n\nGame Over!\n')
                sys.exit(0)

            currentGame.aiPlay()

            try:
                currentGame.gameFile = open(computer_file, 'w')
            except:
                sys.exit('Error opening output file.')

            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()

            print('Game state after move:')
            currentGame.printGameBoard()

            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            if currentGame.pieceCount == 42:
                print('BOARD FULL\n\nGame Over!\n')
                sys.exit(0)

        

    else:
        while(currentGame.pieceCount != 42):
            currentGame.aiPlay()

            try:
                currentGame.gameFile = open(computer_file, 'w')
            except:
                sys.exit('Error opening output file.')

            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()

            print('Game state after move:')
            currentGame.printGameBoard()

            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            if currentGame.pieceCount == 42:
                print('BOARD FULL\n\nGame Over!\n')
                sys.exit(0) 
            
            entry = -1

            while (entry < 1 or entry > 7) or (currentGame.gameBoard[0][entry-1] != 0):
                try:
                    entry = int(input("Choose a move (1-7): "))
                except:
                    entry = -1
                    print('Between 1 and 7...')
                
            currentGame.playPiece(entry-1)

            try:
                currentGame.gameFile = open(human_file, 'w')
            except:
                sys.exit('Error opening output file.')

            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()


            if currentGame.currentTurn == 1:
                currentGame.currentTurn = 2
            elif currentGame.currentTurn == 2:
                currentGame.currentTurn = 1

            print('Game state after move:')
            currentGame.printGameBoard()
            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            if currentGame.pieceCount == 42:
                print('BOARD FULL\n\nGame Over!\n')
                sys.exit(0)
        

    sys.exit('Interactive mode is currently not implemented')


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game
    currentGame.depth = argv[4] # initilize depth

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print ('\nMaxConnect-4 game\n')
    print ('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        computer_file = "computer.txt"
        human_file = "human.txt"
        
        interactiveGame(currentGame, argv[3], computer_file, human_file) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)



