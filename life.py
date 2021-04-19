'''
Le jeu de la vie
Version classique
'''

from tkinter import *
import random
import numpy as np

LINES = 120
COLUMNS = 200
SQUARE_SIZE = 7


def initialiseBoard():
	global board
	global canvas

	for i in range(1, LINES-1):
		for j in range(1, COLUMNS-1):
			p = random.random()
			if p < 0.2:
				board[i][j] = 1 # Alive
				color = 'black'
			else:
				board[i][j] = 0 # Nothing
				color = 'white'
			updateCell(i, j, color)

def updateState(board):
	global canvas

	temp = np.copy(board)

	for i in range(1, LINES-1):
		for j in range(1, COLUMNS-1):
			
			numberNeighbors = board[i-1][j-1] + board[i-1][j] + board[i-1][j+1] + board[i][j-1] + board[i][j+1] + board[i+1][j-1] + board[i+1][j] + board[i+1][j+1]
			
			if board[i][j] == 0 and numberNeighbors == 3:
				temp[i][j] = 1
				updateCell(i, j, 'black')
			elif board[i][j] == 1 and (numberNeighbors != 2 and numberNeighbors != 3):
				temp[i][j] = 0
				updateCell(i, j, 'white')
			else:
				temp[i][j] = board[i][j]

	return temp

def updateCell(i, j, color):
	canvas.itemconfig(rectangles[i-2][j-2], fill=color)



root = Tk()
canvas = Canvas(root, width = COLUMNS*SQUARE_SIZE, height = LINES*SQUARE_SIZE)
canvas.pack()
rectangles = [ [ canvas.create_rectangle (j * SQUARE_SIZE, i * SQUARE_SIZE, j * SQUARE_SIZE + SQUARE_SIZE, i * SQUARE_SIZE + SQUARE_SIZE) for j in range(1, COLUMNS-1)] for i in range(1, LINES-1)]

board = np.zeros((LINES, COLUMNS))

initialiseBoard()
canvas.update()

while True:
	board = updateState(board)
	canvas.update()
