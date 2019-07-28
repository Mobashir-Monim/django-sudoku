from django.shortcuts import render
from django.http import HttpResponse
from random import randint, shuffle
from time import sleep

numberList=[1,2,3,4,5,6,7,8,9]
grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]

puzzle = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]

def sudoku(request):
    global grid
    global puzzle
    grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]
    
    fillGrid(grid)
    row = 0
    
    while row < 9:
        col = 0
        while col < 9:
            puzzle[row][col] = grid[row][col]
            col += 1
        row += 1

    return render(request, 'sudoku/home.html', { 'grids': grid })

def about(request):
    return render(request, 'sudoku/about.html')

def puzzlify(request):
    global puzzle
    num = randint(10, 40)
    x = 0

    while x < num:
        row = randint(0,8)
        col = randint(0,8)

        if puzzle[row][col]:
            puzzle[row][col] = None
            x = x + 1

    return render(request, 'sudoku/home.html', { 'grids': puzzle })

def solution(request):
    global grid
    return render(request, 'sudoku/home.html', { 'grids': grid })

def showPuzzle(request):
    global puzzle
    return render(request, 'sudoku/home.html', { 'grids': puzzle })

def checkGrid(grid):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col]==0:
                return False

    return True 

numberList=[1,2,3,4,5,6,7,8,9]

def fillGrid(grid):
    for i in range(0,81):
        row=i//9
        col=i%9
        if grid[row][col]==0:
            shuffle(numberList)      
            for value in numberList:
                if not(value in grid[row]):
                    if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                        square=[]
                        if row<3:
                            if col<3:
                                square=[grid[i][0:3] for i in range(0,3)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(0,3)]
                            else:  
                                square=[grid[i][6:9] for i in range(0,3)]
                        elif row<6:
                            if col<3:
                                square=[grid[i][0:3] for i in range(3,6)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(3,6)]
                            else:  
                                square=[grid[i][6:9] for i in range(3,6)]
                        else:
                            if col<3:
                                square=[grid[i][0:3] for i in range(6,9)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(6,9)]
                            else:  
                                square=[grid[i][6:9] for i in range(6,9)]
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col]=value
                            if checkGrid(grid):
                                return True
                            else:
                                if fillGrid(grid):
                                    return True
            break
    grid[row][col]=0