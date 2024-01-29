import random
import matplotlib.pyplot as plt

def create_board(width, height):
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

def print_board(board):
    plt.imshow(board, cmap='binary')

def get_neighbour_count(board, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
                count += board[x + i][y + j]
    return count

def update_board(board):
    new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbours = get_neighbour_count(board, i, j)
            if board[i][j]:
                if neighbours in [2, 3]:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
            else:
                if neighbours == 3:
                    new_board[i][j] = 1
    return new_board

def game_of_life(width, height, generations):
    board = create_board(width, height)
    plt.figure()
    for _ in range(generations):
        print_board(board)
        plt.pause(1)  # Pause pour une seconde
        board = update_board(board)
        plt.clf()  # Effacer la figure pour la prochaine génération
    plt.show()

game_of_life(20, 20, 50) # lance une simulation de 50 générations sur un terrain 20x20 avec initialisation aléatoire
