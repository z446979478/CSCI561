import numpy as np
import datetime


def generateState(row,column,wall,stateMatirx):
    for i in range(row):
        for j in range(column):
            stateMatirx[0][0][i][j] = i - 1
            stateMatirx[1][0][i][j] = j
            stateMatirx[0][4][i][j] = i - 2
            stateMatirx[1][4][i][j] = j
            stateMatirx[0][1][i][j] = i + 1
            stateMatirx[1][1][i][j] = j
            stateMatirx[0][5][i][j] = i + 2
            stateMatirx[1][5][i][j] = j
            stateMatirx[0][2][i][j] = i
            stateMatirx[1][2][i][j] = j - 1
            stateMatirx[0][6][i][j] = i
            stateMatirx[1][6][i][j] = j - 2
            stateMatirx[0][3][i][j] = i
            stateMatirx[1][3][i][j] = j + 1
            stateMatirx[0][7][i][j] = i
            stateMatirx[1][7][i][j] = j + 2
            if len(wall) != 0:
                for k in range(len(wall)):
                    if i == 0 or (i == wall[k][0] + 1 and j == wall[k][1]):
                        stateMatirx[0][0][i][j] = i
                        stateMatirx[1][0][i][j] = j
                    if i == 0 or (i == wall[k][0] + 1 and j == wall[k][1]) or i == 1 or (
                            i == wall[k][0] + 2 and j == wall[k][1]):
                        stateMatirx[0][4][i][j] = i
                        stateMatirx[1][4][i][j] = j
                    if i == row - 1 or (i == wall[k][0] - 1 and j == wall[k][1]):
                        stateMatirx[0][1][i][j] = i
                        stateMatirx[1][1][i][j] = j
                    if i == row - 1 or (i == wall[k][0] - 1 and j == wall[k][1]) or i == row - 2 or (
                            i == wall[k][0] - 2 and j == wall[k][1]):
                        stateMatirx[0][5][i][j] = i
                        stateMatirx[1][5][i][j] = j
                    if j == 0 or (j == wall[k][1] + 1 and i == wall[k][0]):
                        stateMatirx[0][2][i][j] = i
                        stateMatirx[1][2][i][j] = j
                    if j == 0 or (j == wall[k][1] + 1 and i == wall[k][0]) or j == 1 or (
                            j == wall[k][1] + 2 and i == wall[k][0]):
                        stateMatirx[0][6][i][j] = i
                        stateMatirx[1][6][i][j] = j
                    if j == column - 1 or (j == wall[k][1] - 1 and i == wall[k][0]):
                        stateMatirx[0][3][i][j] = i
                        stateMatirx[1][3][i][j] = j
                    if j == column - 1 or (j == wall[k][1] - 1 and i == wall[k][0]) or j == column - 2 or (
                            j == wall[k][1] - 2 and i == wall[k][0]):
                        stateMatirx[0][7][i][j] = i
                        stateMatirx[1][7][i][j] = j
            else:
                if i == 0:
                    stateMatirx[0][0][i][j] = i
                    stateMatirx[1][0][i][j] = j
                if i == 0 or i == 1:
                    stateMatirx[0][4][i][j] = i
                    stateMatirx[1][4][i][j] = j
                if i == row - 1:
                    stateMatirx[0][1][i][j] = i
                    stateMatirx[1][1][i][j] = j
                if i == row - 1 or i == row - 2:
                    stateMatirx[0][5][i][j] = i
                    stateMatirx[1][5][i][j] = j
                if j == 0:
                    stateMatirx[0][2][i][j] = i
                    stateMatirx[1][2][i][j] = j
                if j == 0 or j == 1:
                    stateMatirx[0][6][i][j] = i
                    stateMatirx[1][6][i][j] = j
                if j == column - 1:
                    stateMatirx[0][3][i][j] = i
                    stateMatirx[1][3][i][j] = j
                if j == column - 1 or j == column - 2:
                    stateMatirx[0][7][i][j] = i
                    stateMatirx[1][7][i][j] = j


def initialization(rewardMatrix,stateMatirx):

    row = np.array(stateMatirx[0][0])
    col = np.array(stateMatirx[1][0])

    rewardMatrix[2] = rewardMatrix[1][row,col]

    row = np.array(stateMatirx[0][1])
    col = np.array(stateMatirx[1][1])
    rewardMatrix[3] = rewardMatrix[1][row,col]

    row = np.array(stateMatirx[0][2])
    col = np.array(stateMatirx[1][2])
    rewardMatrix[4] = rewardMatrix[1][row,col]

    row = np.array(stateMatirx[0][3])
    col = np.array(stateMatirx[1][3])
    rewardMatrix[5] = rewardMatrix[1][row,col]

    row = np.array(stateMatirx[0][4])
    col = np.array(stateMatirx[1][4])
    rewardMatrix[6] = rewardMatrix[1][row,col]

    row = np.array(stateMatirx[0][5])
    col = np.array(stateMatirx[1][5])
    rewardMatrix[7] = rewardMatrix[1][row,col]

    row = np.array(stateMatirx[0][6])
    col = np.array(stateMatirx[1][6])
    rewardMatrix[8] = rewardMatrix[1][row,col]

    row = np.array(stateMatirx[0][7])
    col = np.array(stateMatirx[1][7])
    rewardMatrix[9] = rewardMatrix[1][row,col]

def caculation(r_walk,r_run,p_walk,p_run,discount,rewardMatrix,stateMatirx,row,column,wall,terminal):
    delta = 0
    p1 = 1 - p_walk
    p2 = 1 - p_run


    v = rewardMatrix[1].copy()


    x0 = (r_walk + discount * rewardMatrix[2])
    x1 = (r_walk + discount * rewardMatrix[3])
    x2 = (r_walk + discount * rewardMatrix[4])
    x3 = (r_walk + discount * rewardMatrix[5])
    x4 = (r_run + discount * rewardMatrix[6])
    x5 = (r_run + discount * rewardMatrix[7])
    x6 = (r_run + discount * rewardMatrix[8])
    x7 = (r_run + discount * rewardMatrix[9])

    #print (rewardMatrix[2])

    a=[
            x0 * p_walk + 0.5 * p1 * x3 + 0.5 * p1 * x2,
            x1 * p_walk + 0.5 * p1 * x3 + 0.5 * p1 * x2,
            x2 * p_walk + 0.5 * p1 * x0 + 0.5 * p1 * x1,
            x3 * p_walk + 0.5 * p1 * x0 + 0.5 * p1 * x1,
            x4 * p_run + 0.5 * p2 * x6 + 0.5 * p2 * x7,
            x5 * p_run + 0.5 * p2 * x6 + 0.5 * p2 * x7,
            x6 * p_run + 0.5 * p2 * x4 + 0.5 * p2 * x5,
            x7 * p_run + 0.5 * p2 * x4 + 0.5 * p2 * x5
    ]
    b = np.array(a)

    rewardMatrix[1] = b.max(axis=0)
    rewardMatrix[0] = b.argmax(axis=0)

    #print (rewardMatrix[1])

    for i in range(len(wall)):
        rewardMatrix[0][wall[i][0]][wall[i][1]] = -1
        rewardMatrix[1][wall[i][0]][wall[i][1]] = 0
    for i in range(len(terminal)):
        x = row - int(terminal[i][0])
        y = int(terminal[i][1]) - 1
        z = float(terminal[i][2])
        rewardMatrix[0][x][y] = -2
        rewardMatrix[1][x][y] = z

    initialization(rewardMatrix, stateMatirx)

    delta = np.max(abs(v - rewardMatrix[1]))
    return delta


def value_iteration(r_walk,r_run,p_walk,p_run,discount,row,column,rewardMatrix,stateMatirx,wall,terminal):
    thresh = 0
    delta = caculation(r_walk, r_run, p_walk, p_run, discount,  rewardMatrix, stateMatirx, row,column,wall,terminal)
    while delta > thresh:
        delta = caculation(r_walk, r_run, p_walk, p_run, discount,  rewardMatrix, stateMatirx, row,column,wall,terminal)

if __name__ == '__main__':
    row = 0
    column = 0
    wall_num = 0
    wall = []
    terminal_num = 0
    terminal = []

    filepath = "input.txt"
    output_path = "output.txt"
    f = open(filepath,'r')
    output_file = open(output_path, 'w')
    for index,line in enumerate(f):
        line = line.replace("\r","")
        line = line.replace("\n","")
        if(index == 0):
            grid_size = [i for i in line.split(",")]
            row = int(grid_size[0])
            column = int(grid_size[1])
        elif (index == 1):
            wall_num = int(line)
        elif(index > 1 and index <= 1 + wall_num):
            wall.append([int(i) for i in line.split(",")])
        elif (index == 2 + wall_num):
            terminal_num = int(line)
        elif(index > 2 + wall_num and index <= 2 + wall_num + terminal_num):
            terminal.append([i for i in line.split(",")])
        elif (index == 3 + wall_num + terminal_num):
            probably = [i for i in line.split(",")]
            p_walk = float(probably[0])
            p_run = float(probably[1])
        elif (index == 4 + wall_num + terminal_num):
            rewards = [i for i in line.split(",")]
            r_walk = float(rewards[0])
            r_run = float(rewards[1])
        else:
            discount = float(line)

    rewardMatrix = np.zeros((10,row,column))
    for i in range(len(wall)):
        x = row - int(wall[i][0])
        y = int(wall[i][1]) - 1
        wall[i][0] = x
        wall[i][1] = y
        rewardMatrix[0][x][y] = -1
        rewardMatrix[1][x][y] = 0
    for i in range(len(terminal)):
        x = row - int(terminal[i][0])
        y = int(terminal[i][1]) - 1
        z = float(terminal[i][2])
        rewardMatrix[0][x][y] = -2
        rewardMatrix[1][x][y] = z

    for i in range(2,10):
        rewardMatrix[i]=rewardMatrix[1].copy()


    stateMatirx = np.zeros((2,8,row,column),dtype = np.int)

    generateState(row, column, wall, stateMatirx)

    initialization(rewardMatrix, stateMatirx)

    value_iteration(r_walk, r_run, p_walk, p_run, discount, row, column, rewardMatrix, stateMatirx,wall,terminal)

    for m in range(row):
        for n in range(column):
            if rewardMatrix[0][m][n] == 0:
                output_file.write("Walk Up")
            elif rewardMatrix[0][m][n] == 1:
                output_file.write("Walk Down")
            elif rewardMatrix[0][m][n] == 2:
                output_file.write("Walk Left")
            elif rewardMatrix[0][m][n] == 3:
                output_file.write( "Walk Right")
            elif rewardMatrix[0][m][n] == 4:
                output_file.write("Run Up")
            elif rewardMatrix[0][m][n] == 5:
                output_file.write("Run Down")
            elif rewardMatrix[0][m][n] == 6:
                output_file.write("Run Left")
            elif rewardMatrix[0][m][n] == 7:
                output_file.write("Run Right")
            elif rewardMatrix[0][m][n] == -2:
                output_file.write("Exit")
            elif rewardMatrix[0][m][n] == -1:
                output_file.write( "None")
            if n != column - 1:
                output_file.write(",")
        output_file.write("\n")