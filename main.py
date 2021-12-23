import pygame as pg
import numpy as np


def init_random():
    board = np.random.randint(2, size=(resolution[0] // scale, resolution[1] // scale))
    for i, rows in enumerate(board):
        for j, columns in enumerate(rows):
            if i == 0 or j == 0 or i == game[0] - 1 or j == game[1] - 1:
                board[i][j] = 0
    return board


def init_glider():
    board = np.zeros((resolution[0] // scale, resolution[1] // scale))
    board[10][10] = 1
    board[10][11] = 1
    board[10][12] = 1
    board[11][10] = 1
    board[12][11] = 1
    return board


def update(board):
    temp_board = np.copy(board)
    for i, rows in enumerate(board):
        if i in (0, game[0] - 1):
            continue
        for j, columns in enumerate(rows):
            if j in (0, game[1] - 1):
                continue
            alive = board[i - 1][j - 1] + board[i - 1][j] + board[i - 1][j + 1] + board[i][j - 1] + 0 + board[i][j + 1] + board[i + 1][j - 1] + board[i + 1][j] + board[i + 1][j + 1]
            if board[i][j] and (alive == 2 or alive == 3):
                temp_board[i][j] = 1
            elif not board[i][j] and alive == 3:
                temp_board[i][j] = 1
            else:
                temp_board[i][j] = 0
    return temp_board


resolution = (1200, 700)
scale = 5
game = (resolution[0] // scale, resolution[1] // scale)

pg.init()
font = pg.font.SysFont(None, 48)
img = font.render(f"Alive pixels: {scale}", True, (255, 255, 255))

windows = pg.display.set_mode(resolution)
pixels = init_random()
# pixels = init_glider()
iteration = 0

running = True

while running:
    pixels = update(pixels)
    surface = pg.surfarray.make_surface(pixels * 253)
    surface = pg.transform.scale(surface, (resolution[0], resolution[1]))
    img = font.render(f"Alive pixels: {np.sum(pixels)}", True, (255, 255, 255))
    img2 = font.render(f"Iteration: {iteration}", True, (255, 255, 255))
    windows.blit(surface, (0, 0))
    windows.blit(img, (20, 20))
    windows.blit(img2, (20, 60))
    pg.display.update()
    iteration += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
