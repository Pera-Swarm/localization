import numpy as np
import cv2

# Chessboard size (number of squares)
rows = 7
cols = 8
square_size = 100  # pixels per square

board = np.zeros((rows * square_size, cols * square_size), dtype=np.uint8)

for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            board[i*square_size:(i+1)*square_size,
                  j*square_size:(j+1)*square_size] = 255

cv2.imwrite("chessboard_8x7.png", board)
