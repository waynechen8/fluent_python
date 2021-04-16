# -*- coding: utf-8 -*-

l = [1, 2, 3]
l * 5
print(5 * 'abcd')

board = [['_'] * 3 for i in range(3)]
print("board:", board)
board[1][2] = 'X'
print("board:", board)

weird_board = [['_'] * 3 ] * 3
print("weird board:", weird_board)
weird_board[1][2] = 'O'
print("weird board:", weird_board)
