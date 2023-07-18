#!/usr/bin/python3
"""The N queens puzzle
Class to solve the N puzzle challenge

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
"""
import sys


def init_board(n):
    """Initialize chessboard with empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def sol_board(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def safe_spot(board, row, col):
    """Function to check if a queen can
    be placed at the specified position

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    n = len(board)
    # X out all spots horizontally
    for c in range(n):
        if c != col:
            board[row][c] = 'x'
    # X out all spots vertically
    for r in range(n):
        if r != row:
            board[r][col] = 'x'
    # X out all spots diagonally
    for i in range(n):
        for j in range(n):
            if i != row and j != col and abs(i - row) == abs(j - col):
                board[i][j] = 'x'


def r_sol(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions (list): A list of lists containing solutions.
    """
    n = len(board)
    if queens == n:
        solutions.append(sol_board(board))
        return solutions

    for c in range(n):
        if board[row][c] == " ":
            tmp_board = [row[:] for row in board]  # Create a copy of the board
            tmp_board[row][c] = "Q"
            safe_spot(tmp_board, row, c)
            solutions = r_sol(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    """
    Check if the correct number of arguments is provided
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = r_sol(board, 0, 0, [])
    for sol in solutions:
        print(sol)
