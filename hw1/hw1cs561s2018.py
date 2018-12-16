import sys
from copy import copy, deepcopy
import re

class AlphaBetaPruning(object):

    def __init__(self,player,depth,newboard):
        self.player = player
        self.max_depth = depth
        self.newboard = newboard
        self.game = game()
        self.number = 0

    def getResult(self):
        result = self.maxValue("-Infinity","Infinity", self.player, self.newboard, self.max_depth, 0)
        return(result[1],result[0],self.number )

    def minValue(self,alpha,beta,current_player,current_board_state,depth,num_pass):
        x = 0
        y = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if ('S' in current_board_state[i][j][0]):
                    x = 1
                if ('C' in current_board_state[i][j][0]):
                    y = 1

        if depth <= 0 or num_pass == 2 or x == 0 or y == 0:
            utility_value = self.game.calculateScore(self.player, current_board_state)
            self.number += 1
            return (utility_value,None)

        min_score = "Infinity"
        selected_action = None

        opponent = self.game.getOpponent(current_player)
        actions,list3 = self.game.getMovements(current_player,current_board_state)


        if (len(list3) == 0):
            list3 = [None]
            num_pass = num_pass + 1
        else:
            num_pass = 0

        self.number += 1

        for list in list3:
            if (list is not None):
                new_bs = self.game.move(current_player,list[1][0],list[1][1],current_board_state,list[0][0],list[0][1])
                score = self.maxValue(alpha, beta, opponent, new_bs, depth - 1, num_pass)[0]
            else:
                new_bs = deepcopy(current_board_state)
                score = self.maxValue(alpha, beta, opponent, new_bs, depth - 1, num_pass)[0]
            if self.game.compare(score, min_score) == -1:
                min_score = score
                selected_action = list

            beta_to_update = min_score if self.game.compare(beta,min_score) == 1 else beta

            if self.game.compare(beta_to_update, alpha) > 0:
                beta = beta_to_update

            if self.game.compare(min_score, alpha) <= 0:
                return (min_score, selected_action)

        return(min_score,selected_action)

    def maxValue(self,alpha,beta,current_player,current_board_state,depth,num_pass):
        x = 0
        y = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if ('S' in current_board_state[i][j][0]):
                    x = 1
                if ('C'in current_board_state[i][j][0]):
                    y = 1
        if depth <= 0 or num_pass == 2 or x == 0 or y == 0:
            utility_value = self.game.calculateScore(self.player, current_board_state)
            self.number += 1
            return (utility_value, None)

        max_score = "-Infinity"
        selected_action = None

        opponent = self.game.getOpponent(current_player)
        actions,list3 = self.game.getMovements(current_player,current_board_state)

        if(len(list3) == 0):
            list3= [None]
            num_pass = num_pass + 1
        else:
            num_pass = 0

        self.number += 1


        for list in list3:
            if(list is not None):
                new_bs = self.game.move(current_player,list[1][0],list[1][1],current_board_state,list[0][0],list[0][1])
                score = self.minValue(alpha, beta, opponent, new_bs, depth - 1, num_pass)[0]
            else:
                new_bs = deepcopy(current_board_state)
                score = self.minValue(alpha, beta, opponent, new_bs, depth - 1, num_pass)[0]
            if self.game.compare(score, max_score) == 1:
                max_score = score
                selected_action = list

            alpha_to_update = max_score if self.game.compare(alpha,max_score) == -1 else alpha

            if self.game.compare(alpha_to_update, beta) < 0:
                alpha = alpha_to_update

            if self.game.compare(max_score, beta) >= 0:
                return (max_score, selected_action)

        return(max_score,selected_action)

class MiniMaxSearch(object):

    def __init__(self,player,depth,newboard):
        self.player = player
        self.max_depth = depth
        self.newboard = newboard
        self.game = game()
        self.number = 0

    def getResult(self):
        result = self.maxValue(self.player, self.newboard, self.max_depth,0)
        return(result[1],result[0],self.number )

    def minValue(self,current_player,current_board_state,depth,num_pass):
        x = 0
        y = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if ('S' in current_board_state[i][j][0]):
                    x = 1
                if ('C' in current_board_state[i][j][0]):
                    y = 1

        if depth <= 0 or num_pass == 2 or x == 0 or y == 0:
            utility_value = self.game.calculateScore(self.player, current_board_state)
            self.number += 1
            return (utility_value,None)

        min_score = "Infinity"
        selected_action = None

        opponent = self.game.getOpponent(current_player)
        actions,list3 = self.game.getMovements(current_player,current_board_state)


        if (len(list3) == 0):
            list3 = [None]
            num_pass = num_pass + 1
        else:
            num_pass = 0

        self.number += 1

        for list in list3:
            if (list is not None):
                new_bs = self.game.move(current_player,list[1][0],list[1][1],current_board_state,list[0][0],list[0][1])
                score = self.maxValue(opponent, new_bs, depth - 1, num_pass)[0]
            else:
                new_bs = deepcopy(current_board_state)
                score = self.maxValue(opponent, new_bs, depth - 1, num_pass)[0]
            if self.game.compare(score, min_score) == -1:
                min_score = score
                selected_action = list

        return(min_score,selected_action)

    def maxValue(self,current_player,current_board_state,depth,num_pass):
        x = 0
        y = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if ('S' in current_board_state[i][j][0]):
                    x = 1
                if ('C'in current_board_state[i][j][0]):
                    y = 1
        if depth <= 0 or num_pass == 2 or x == 0 or y == 0:
            utility_value = self.game.calculateScore(self.player, current_board_state)
            self.number += 1
            return (utility_value, None)

        max_score = "-Infinity"
        selected_action = None

        opponent = self.game.getOpponent(current_player)
        actions,list3 = self.game.getMovements(current_player,current_board_state)

        if(len(list3) == 0):
            list3 = [None]
            num_pass = num_pass + 1
        else:
            num_pass = 0

        self.number += 1

        for list in list3:
            if(list is not None):
                new_bs = self.game.move(current_player,list[1][0],list[1][1],current_board_state,list[0][0],list[0][1])
                score = self.minValue(opponent, new_bs, depth - 1, num_pass)[0]
            else:
                new_bs = deepcopy(current_board_state)
                score = self.minValue(opponent, new_bs, depth - 1, num_pass)[0]
            if self.game.compare(score, max_score) == 1:
                max_score = score
                selected_action = list

        return(max_score,selected_action)

class game():

    def compare(self,a,b):
        if (type(a) is not str and type(b) is not str):
            if a > b:
                return 1
            elif a < b:
                return -1
            return 0
        if (type(a) is str and type(b) is str):
            if a == b:
                return 0
            if a == "-Infinity":
                return -1
            return 1
        if (type(a) is str):
            if a == "-Infinity":
                return -1
            return 1
        if b == "-Infinity":
            return 1
        return -1

    def getOpponent(self,player):
        opponent_player = 'C' if player == 'S' else 'S'
        return(opponent_player)

    def getMovements(self,player,newboard):
        if(player == 'S'):
            list = []
            list3 = []
            for i in range(0, 8):
                for j in range(0, 8):
                    if ('S'in newboard[i][j][0] ):
                        if ((0<i<=7)&(0<j<=7)):
                            if((newboard[i-1][j-1][0]=='0')|((newboard[i-1][j-1][0]=='S')&(i==1))):
                                list.append((i - 1,j - 1))
                                list2 = []
                                list2.append((i,j))
                                list2.append((i-1, j-1))
                                list3.append(list2)
                        if ((1<i<=7)&(1<j<=7)):
                            if ((newboard[i - 1][j - 1][0] == 'C')& ((newboard[i-2][j-2][0]=='0')|((newboard[i - 2][j - 2][0] == 'S') & (i == 2)))):
                                list.append((i - 2,j - 2))
                                list2 = []
                                list2.append((i,j))
                                list2.append((i-2, j-2))
                                list3.append(list2)
                        if ((0<i<=7)&(0<=j<7)):
                            if ((newboard[i - 1][j + 1][0] == '0') | ((newboard[i - 1][j + 1][0] == 'S') & (i == 1))):
                                list.append((i - 1, j + 1))
                                list2 = []
                                list2.append((i, j))
                                list2.append((i - 1, j +1))
                                list3.append(list2)
                        if ((1<i<=7)&(0<=j<6)):
                            if ((newboard[i - 1][j + 1][0] == 'C') & ((newboard[i - 2][j + 2][0] == '0') | ((newboard[i - 2][j + 2][0] == 'S') & (i == 2)))):
                                list.append((i - 2,j + 2))
                                list2 = []
                                list2.append((i,j))
                                list2.append((i-2, j+2))
                                list3.append(list2)
            return list,list3

        if (player == 'C'):
            list = []
            list3 = []
            for i in range(0, 8):
                for j in range(0, 8):
                    if ('C'in newboard[i][j][0]):
                        if ((0 <= i < 7) & (0 < j <= 7)):
                            if ((newboard[i + 1][j - 1][0] == '0') | ((newboard[i + 1][j - 1][0] == 'C') & (i == 6))):
                                list.append((i + 1, j - 1))
                                list2 = []
                                list2.append((i, j))
                                list2.append((i + 1, j - 1))
                                list3.append(list2)
                        if ((0 <= i < 6) & (1 < j <= 7)):
                            if ((newboard[i + 1][j - 1][0] == 'S') & ((newboard[i + 2][j - 2][0] == '0') | ((newboard[i + 2][j - 2][0] == 'C') & (i == 5)))):
                                list.append((i + 2, j - 2))
                                list2 = []
                                list2.append((i, j))
                                list2.append((i + 2, j - 2))
                                list3.append(list2)
                        if ((0 <= i < 7) & (0 <= j < 7)):
                            if ((newboard[i + 1][j + 1][0] == '0') | ((newboard[i + 1][j + 1][0] == 'C') & (i == 6))):
                                list.append((i + 1, j + 1))
                                list2 = []
                                list2.append((i, j))
                                list2.append((i + 1, j + 1))
                                list3.append(list2)
                        if ((0 <= i < 6) & (0 <= j < 6)):
                            if ((newboard[i + 1][j + 1][0] == 'S') & ((newboard[i + 2][j + 2][0] == '0') | ((newboard[i + 2][j + 2][0] == 'C') & (i == 5)))):
                                list.append((i + 2, j + 2))
                                list2 = []
                                list2.append((i, j))
                                list2.append((i + 2, j + 2))
                                list3.append(list2)
            return list,list3

    def move(self,player,i,j,newboard,i0,j0):

        result_newboard = deepcopy(newboard)
        result_newboard[i][j][0] = player
        result_newboard[i][j][1] += 1
        result_newboard[i0][j0][0]= '0'
        result_newboard[i0][j0][1] -= 1

        if ((i0 - i == 2) & (j0 - j == 2)):
            result_newboard[i0-1][j0-1][0] = '0'
            result_newboard[i0-1][j0-1][1] -= 1
        if ((i0 - i == 2) & (j - j0 == 2)):
            result_newboard[i0 - 1][j - 1][0] = '0'
            result_newboard[i0 - 1][j - 1][1] -= 1
        if ((i - i0 == 2) & (j0 - j == 2)):
            result_newboard[i - 1][j0 - 1][0] = '0'
            result_newboard[i - 1][j0 - 1][1] -= 1
        if ((i - i0 == 2) & (j - j0 == 2)):
            result_newboard[i - 1][j - 1][0] = '0'
            result_newboard[i - 1][j - 1][1] -= 1
        return (result_newboard)

    def calculateScore(self,player,newboard):
        total1 = 0
        total2 = 0
        i=0
        j=0
        m=0
        n=0
        if player == 'S':
            for i in range (8):
                for j in range(8):
                    if newboard[i][j][0] == 'S':
                        total1 += newboard[i][j][1] * newboard[i][j][3]
                    if newboard[i][j][0] == 'C':
                        total2 += newboard[i][j][1] * newboard[i][j][2]
        if player == 'C':
            for m in range (8):
                for n in range(8):
                    if newboard[m][n][0] == 'S':
                        total2 += newboard[m][n][1] * newboard[m][n][3]
                    if newboard[m][n][0] == 'C':
                        total1 += newboard[m][n][1] * newboard[m][n][2]
        return total1 - total2

if __name__ == '__main__':

    player = ""
    task = ""
    max_depth = -1
    board_state = []
    value = []

    filepath = "input.txt"
    output_path = "output.txt"
    f = open(filepath,'r')
    for index,line in enumerate(f):
        line = line.replace("\r","")
        line = line.replace("\n","")
        if(index == 0):
            if 'Star' in line:
                player = 'S'
            elif 'Circle' in line:
                player = 'C'
            else:
                player = '0'
        elif (index == 1):
            task = line
        elif(index == 2):
            max_depth = int(line)
        elif(index == 11):
            value = [i for i in line.split(",")]
            value = list(map(int, value))
        else:
            rows = [i for i in line.split(",")]
            board_state.append(rows)

    if(max_depth > 10):
        print("max depth should be less than 10")
        exit()
    for k in range(0, 7):
        if (value[k] > value[k+1]):
            print("Row values should be increasing")
            exit()

    board_player = ''
    number = 0
    newboard = [[0 for col in range(8)] for row in range(8)]
    for i in range(0, 8):
        for j in range(0, 8):
            if board_state[i][j] == '0':
                board_player = '0'
                number = 0
            if 'S' in board_state[i][j]:
                board_player = 'S'
                b = re.findall(r"\d+\.?\d*", board_state[i][j])
                number = list(map(int, b))[0]
            if 'C' in board_state[i][j]:
                board_player = 'C'
                b = re.findall(r"\d+\.?\d*", board_state[i][j])
                number = list(map(int, b))[0]
            newboard[i][j] = [board_player, number, value[i], value[7-i]]
    list=[]
    mylist=[]

    output_file = open(output_path, 'w')

    if (task == "MINIMAX"):
        minimax_search = MiniMaxSearch(player, max_depth, newboard)
    if (task == "ALPHABETA"):
        minimax_search = AlphaBetaPruning(player,max_depth,newboard)

    movement,score,node_number = minimax_search.getResult()
    if(movement is None):
        output_file.write("pass"+ "\n")
    else:
        output_file.write("{0}{1}-{2}{3}".format(chr(72-movement[0][0]).upper(),movement[0][1]+1,chr(72-movement[1][0]).upper(),movement[1][1]+1)+ "\n")


    game = game()
    if(movement is not None):
        newboard = game.move(player,movement[1][0],movement[1][1],newboard,movement[0][0],movement[0][1])

    output_file.write(str(game.calculateScore(player, newboard))+ "\n")
    output_file.write(str(score)+ "\n")
    output_file.write(str(node_number))
