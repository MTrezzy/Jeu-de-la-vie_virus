from tkinter import *
import random
import time

LINES = 100
COLUMNS = 170
SQUARE_SIZE = 7

def on_click(event):
	global board
	global canvas

	updateState()
	displayBoard()
	canvas.update()
   

def initialiseBoard():
	global board

	for i in range(1, LINES-1):
		for j in range(1, COLUMNS-1):
			p = random.random()
			if p < 0.2:
				board[i][j] = 1 # Alive
			else:
				board[i][j] = 0 # Nothing

def displayBoard(): 
	global board
	global canvas

	for i in range(1, LINES-1):
		for j in range(1, COLUMNS-1):
			if board[i][j] == 1:
				color = 'black'
			else:
				color = 'white'
			canvas.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE, j * SQUARE_SIZE + SQUARE_SIZE, i * SQUARE_SIZE + SQUARE_SIZE, fill=color)

def updateState():
	global board
	global temp

	for i in range(1, LINES-1):
		for j in range(1, COLUMNS-1):
			
			numberNeighbors = board[i-1][j-1] + board[i-1][j] + board[i-1][j+1] + board[i][j-1] + board[i][j+1] + board[i+1][j-1] + board[i+1][j] + board[i+1][j+1]
			if board[i][j] == 0 and numberNeighbors == 3:
				temp[i][j] = 1
			elif board[i][j] == 1 and (numberNeighbors != 2 and numberNeighbors != 3):
				temp[i][j] = 0
			else:
				temp[i][j] = board[i][j]

	for i in range(1, LINES-1):
		for j in range(1, COLUMNS-1):
			board[i][j] = temp[i][j]


root = Tk()
canvas = Canvas(root, width = COLUMNS*SQUARE_SIZE, height = LINES*SQUARE_SIZE)
canvas.pack()

board = [ [0]*COLUMNS for _ in range(LINES) ]
temp = [ [0]*COLUMNS for _ in range(LINES) ]

initialiseBoard()
displayBoard()

canvas.update()
canvas.bind('<Button-1>', on_click)

root.mainloop()
