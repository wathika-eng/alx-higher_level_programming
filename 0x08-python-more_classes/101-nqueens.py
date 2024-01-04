#!/usr/bin/python3
import sys

"""N queens""" ""


def is_safe(board, row, col, N):
    """Check if a queen can be placed on board[row][col]
    Args:
        board (list): The board.
        row (int): The row.
        col (int): The column.
        N (int): The size of the board.
    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i][col] == "Q":
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == "Q":
            return False

    return True


def solve_nqueens(N):
    """Solve the N queens problem.
    Args:
        N (int): The size of the board.
    Returns:
        list: List of solutions.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [["." for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve_queens_util(board, row):
        """Solve the N queens problem.
        Args:
            board (list): The board.
            row (int): The row.
        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        if row == N:
            solutions.append(["".join(row) for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = "Q"
                solve_queens_util(board, row + 1)
                board[row][col] = "."

    solve_queens_util(board, 0)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    solve_nqueens(N)
