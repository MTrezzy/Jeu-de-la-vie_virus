'''
Le jeu de la vie
Version virus
'''

from tkinter import *
import random
import numpy as np


LINES       = 60
COLUMNS     = 100
SQUARE_SIZE = 10
NB_VIRUS    = 3


def initialiseBoard():
	global board
	global canvas

	for i in range(1, LINES-1):
		for j in range(1, COLUMNS-1):
			p = random.random()
			if p < 0.5:
				board[i][j] = 1 # Alive
				color = 'black'
			else:
				board[i][j] = 0 # Nothing
				color = 'white'
			updateCell(i, j, color)
	
	for i in range(NB_VIRUS):
		x = random.randint(1, LINES-1)
		y = random.randint(1, COLUMNS-1)
		board[x][y] = 3
		updateCell(x, y, 'red')


def updateState(board):
	global canvas

	temp = np.copy(board)

	for i in range(1, LINES-1):
		for j in range(1, COLUMNS-1):
			
			neighborsList = [board[i-1][j-1], board[i-1][j], board[i-1][j+1], board[i][j-1], board[i][j+1], board[i+1][j-1], board[i+1][j], board[i+1][j+1]]
			virus = neighborsList.count(3)
			p = random.random()

			if board[i][j] == 0:
				if neighborsList.count(3) + neighborsList.count(2) + neighborsList.count(1) == 3:
					temp[i][j] = 1
					updateCell(i, j, 'white')

			elif board[i][j] == 1: # Normal
				if virus > 0:
					if p < virus*0.3:
						temp[i][j] = 3
						updateCell(i, j, 'red')
	
			elif board[i][j] == 3: # Virus
				if p < 0.1:
					temp[i][j] = 0
					updateCell(i, j, 'white')
				elif p > 0.85:
					temp[i][j] = 2
					updateCell(i, j, 'green')

			elif board[i][j] == 2: # Immunity
				if virus > 0:
					if p < virus*0.05:
						temp[i][j] = 3
						updateCell(i, j, 'red')
				elif p < 0.1:
					temp[i][j] = 1
					updateCell(i, j, 'black')

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
