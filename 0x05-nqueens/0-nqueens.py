#!/usr/bin/python3

import sys

"""Function to check if placing a queen at a specific position is safe"""
def is_safe(board, row, col, N):
    for i in range(row):
        """Check if there's a queen in the same column or in the diagonal"""
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

"""Function to solve the N Queens problem using backtracking"""
def solve_nqueens(board, row, N):
    """If all N rows are filled, we found a solution, print it"""
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    """Try placing the queen in each column of the current row"""
    for col in range(N):
        if is_safe(board, row, col, N):
            """If it's safe, mark the position and move to the next row"""
            board[row] = col
            solve_nqueens(board, row + 1, N)

"""Main function to handle input and call the solving function"""
def nqueens(N):
    """Input validation"""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """Create an array to represent the board. -1 means no queen in that row."""
    board = [-1] * N
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    """Check if the number of arguments is correct"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

