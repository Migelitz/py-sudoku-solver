from solver import SudokuSolver

grid = [[7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]]

def show_board(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[row][col], end=' ')
        print()
        
show_board(grid)

solver = SudokuSolver(grid)

print("=========================================")
solved = solver.solve()
show_board(grid)