"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:

    # check horizontal
    for row in board:
        unique = set(row)
        if len(unique) == 1 and unique != "-":
            return f"{row[0]} wins!"

    # check verticals
    for i in range(3):
        col = [row[i] for row in board]
        unique = set(col)
        if len(unique) == 1 and unique != "-":
            return f"{col[0]} wins!"

    # check diag
    # 1
    unique = set([board[i][i] for i in range(3)])
    if len(unique) == 1 and unique != "-":
        return f"{board[0][0]} wins!"
    # 2
    unique = set(board[i][2 - i] for i in range(3))
    if len(unique) == 1 and unique != "-":
        return f"{board[0][2]} wins!"

    if "-" in [el for row in board for el in row]:
        return "unfinished!"
    else:
        return "draw!"


if __name__ == "__main__":
    deck_1 = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]

    deck_2 = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]

    print(tic_tac_toe_checker(deck_1))
