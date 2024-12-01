import random
from math import *
from agents.baselines.baseline2 import Agent

"""
    You "should" modify this file.
"""

def find (board, i, j, m, n, my_s, win_len):
    mylist = [0, 0, 0, 0]
    count = 0
    row = 0
    x = j
    while x < n and board[i][x] == my_s:
        count += 1
        x += 1
    x = j - 1
    while x >= 0 and board[i][x] == my_s:
        count += 1
        x -= 1
    row = count
    mylist[0] = row
    count = 0
    col = 0
    y = i
    while y < m and board[y][j] == my_s:
        count += 1
        y += 1
    y = i - 1
    while y >= 0 and board[y][j] == my_s:
        count += 1
        y -= 1
    col = count
    mylist[1] = col
    count = 0
    dia = 0
    x = j
    y = i
    while x >= 0 and y < m and board[y][x] == my_s:
        count += 1
        x -= 1
        y += 1
    x = j + 1
    y = i - 1
    while x < n and y >= 0 and board[y][x] == my_s:
        count += 1
        x += 1
        y -= 1
    dia = count
    mylist[2] = dia
    count = 0
    a_dia = 0
    x = j
    y = i
    while x < n and y < m and board[y][x] == my_s:
        count += 1
        x += 1
        y += 1
    x = j - 1
    y = i - 1
    while x >= 0 and y >= 0 and board[y][x] == my_s:
        count += 1
        x -= 1
        y -= 1
    a_dia = count
    mylist[3] = a_dia
    if win_len > 3:
        count = 0
        x = j
        while x < n and (board[i][x] == 0 or board[i][x] == my_s):
            count += 1
            x += 1
        x = j - 1
        while x >= 0 and (board[i][x] == 0 or board[i][x] == my_s):
            count += 1
            x -= 1
        if count < win_len:
            mylist[0] = 0
        y = i
        count = 0
        while y < m and (board[y][j] == 0 or board[y][j] == my_s):
            count += 1
            y += 1
        y = i - 1
        while y >= 0 and (board[y][j] == 0 or board[y][j] == my_s):
            count += 1
            y -= 1
        if count < win_len:
            mylist[1] = 0
        x = j
        y = i
        count = 0
        while y < m and x >= 0 and (board[y][x] == 0 or board[y][x] == my_s):
            count += 1
            x -= 1
            y += 1
        x = j + 1
        y = i - 1
        while y >= 0 and x < n and (board[y][x] == 0 or board[y][x] == my_s):
            count += 1
            x += 1
            y -= 1
        if count < win_len:
            mylist[2] = 0
        x = j
        y = i
        count = 0
        while y < m and x < n and (board[y][x] == 0 or board[y][x] == my_s):
            count += 1
            x += 1
            y += 1
        x = j - 1
        y = i - 1
        while y >= 0 and x >= 0 and (board[y][x] == 0 or board[y][x] == my_s):
            count += 1
            x -= 1
            y -= 1
        if count < win_len:
            mylist[3] = 0
    mylist.sort()
    mylist.reverse()
    return mylist

def opponent (board, i, j, m, n, my_s, win_len):
    mylist = [0, 0, 0, 0]
    count = 0
    row = 0
    x = j
    while x < n and (board[i][x] != my_s and board[i][x] != 0):
        count += 1
        x += 1
    x = j - 1
    while x >= 0 and (board[i][x] != my_s and board[i][x] != 0):
        count += 1
        x -= 1
    row = count
    mylist[0] = row
    count = 0
    col = 0
    y = i
    while y < m and (board[y][j] != my_s and board[y][j] != 0):
        count += 1
        y += 1
    y = i - 1
    while y >= 0 and (board[y][j] != my_s and board[y][j] != 0):
        count += 1
        y -= 1
    col = count
    mylist[1] = col
    count = 0
    dia = 0
    x = j
    y = i
    while x >= 0 and y < m and (board[y][x] != my_s and board[y][x] != 0):
        count += 1
        x -= 1
        y += 1
    x = j + 1
    y = i - 1
    while x < n and y >= 0 and (board[y][x] != my_s and board[y][x] != 0):
        count += 1
        x += 1
        y -= 1
    dia = count
    mylist[2] = dia
    count = 0
    a_dia = 0
    x = j
    y = i
    while x < n and y < m and (board[y][x] != my_s and board[y][x] != 0):
        count += 1
        x += 1
        y += 1
    x = j - 1
    y = i - 1
    while x >= 0 and y >= 0 and (board[y][x] != my_s and board[y][x] != 0):
        count += 1
        x -= 1
        y -= 1
    a_dia = count
    mylist[3] = a_dia
    if win_len > 3:
        count = 0
        x = j
        while x < n and (board[i][x] != my_s):
            count += 1
            x += 1
        x = j - 1
        while x >= 0 and (board[i][x] != my_s):
            count += 1
            x -= 1
        if count < win_len:
            mylist[0] = 0
        y = i
        count = 0
        while y < m and (board[y][j] != my_s):
            count += 1
            y += 1
        y = i - 1
        while y >= 0 and (board[y][j] != my_s):
            count += 1
            y -= 1
        if count < win_len:
            mylist[1] = 0
        x = j
        y = i
        count = 0
        while y < m and x >= 0 and (board[y][x] != my_s):
            count += 1
            x -= 1
            y += 1
        x = j + 1
        y = i - 1
        while y >= 0 and x < n and (board[y][x] != my_s):
            count += 1
            x += 1
            y -= 1
        if count < win_len:
            mylist[2] = 0
        x = j
        y = i
        count = 0
        while y < m and x < n and (board[y][x] != my_s):
            count += 1
            x += 1
            y += 1
        x = j - 1
        y = i - 1
        while y >= 0 and x >= 0 and (board[y][x] != my_s):
            count += 1
            x -= 1
            y -= 1
        if count < win_len:
            mylist[3] = 0
    mylist.sort()
    mylist.reverse()
    return mylist

def nonzero (board, i, j, m, n, my_s):
    mylist = [0, 0, 0, 0]
    count = 0
    row = 0
    x = j
    while x < n and board[i][x] != 0:
        count += 1
        x += 1
    x = j - 1
    while x >= 0 and board[i][x] != 0:
        count += 1
        x -= 1
    row = count
    mylist[0] = row
    count = 0
    col = 0
    y = i
    while y < m and board[y][j] != 0:
        count += 1
        y += 1
    y = i - 1
    while y >= 0 and board[y][j] != 0:
        count += 1
        y -= 1
    col = count
    mylist[1] = col
    count = 0
    dia = 0
    x = j
    y = i
    while x >= 0 and y < m and board[y][x] != 0:
        count += 1
        x -= 1
        y += 1
    x = j + 1
    y = i - 1
    while x < n and y >= 0 and board[y][x] != 0:
        count += 1
        x += 1
        y -= 1
    dia = count
    mylist[2] = dia
    count = 0
    a_dia = 0
    x = j
    y = i
    while x < n and y < m and board[y][x] != 0:
        count += 1
        x += 1
        y += 1
    x = j - 1
    y = i - 1
    while x >= 0 and y >= 0 and board[y][x] != 0:
        count += 1
        x -= 1
        y -= 1
    a_dia = count
    mylist[3] = a_dia
    mylist.sort()
    mylist.reverse()
    return mylist

class Agent(Agent):
    def __init__(self, name, symbol, game_config):
        super().__init__(name, symbol, game_config)
    
    def get_move(self, board):
        # Implement your agent here
        moves = self.find_available_moves(board)
        for col in moves:
            updated_board = self.update_board(board, col)
            if self.is_winner(updated_board):
                return col    
        my_s = self.symbol
        m = len (board)
        n = len (board[0])
        total = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] != 0:
                    total += 1
        win_len = self.game_config["win_n"]
        flag = True
        j = floor (floor (n / 2) * (win_len - 3) / (n - 3))
        mylist = [-1, 0, 0, 0, j]
        o_list = [-1, 0, 0, 0, j]
        zero_list = [-1, 0, 0, 0, j] 
        for count_times in range (n):
            if board[0][j] == 0:
                for i in range (m):
                    if board[m - 1 - i][j] != 0:
                        continue
                    else:
                        board[m - 1 - i][j] = my_s
                        flag_test = True
                        
                        for j_test in range (n):
                            if board[0][j_test] == 0:
                                for i_test in range(m):
                                    if board[m - 1 - i_test][j_test] != 0:
                                        continue
                                    else:
                                        board[m - 1 - i_test][j_test] = my_s * 2
                                        list_test = opponent (board, m - 1 - i_test, j_test, m, n, my_s, win_len)
                                        if list_test[0] >= win_len:
                                            flag_test = False
                                        board[m - 1 - i_test][j_test] = 0
                                        break
                                if flag_test == False:
                                    break
                        if flag_test == False:
                            board[m - 1 - i][j] = 0
                            break
                   
                        cur_list = find (board, m - 1 - i, j, m, n, my_s, win_len)
                        cur_zero_list = nonzero (board, m - 1 - i, j, m, n, my_s)
                        board[m - 1 - i][j] = my_s * 2
                        cur_o_list = opponent (board, m - 1 - i, j, m, n, my_s, win_len)
                        if flag == True:
                            cur_list.append(j)
                            mylist = cur_list.copy()
                            cur_o_list.append(j)
                            o_list = cur_o_list.copy()
                            cur_zero_list.append(j)
                            zero_list = cur_zero_list.copy()
                            flag = False
                        else:
                            flag1 = True
                            if total >= floor (n * m / 3) and total < floor (n * m / 3) + 12:
                                for k in range(4):
                                    if (cur_list[k] < mylist[k] and cur_list[k] != 0):
                                        cur_list.append(j)
                                        mylist = cur_list.copy()
                                        zero_list = cur_zero_list.copy()
                                        zero_list.append(j)
                                        flag1 = False
                                        break
                                    elif (cur_list[k] > mylist[k]):
                                        flag1 = False
                                        break
                            else:
                                for k in range(4):
                                    if (cur_list[k] > mylist[k]):
                                        cur_list.append(j)
                                        mylist = cur_list.copy()
                                        zero_list = cur_zero_list.copy()
                                        zero_list.append(j)
                                        flag1 = False
                                        break
                                    elif (cur_list[k] < mylist[k]):
                                        flag1 = False
                                        break
                            
                            if flag1 == True:
                                for k in range(4):
                                    if (cur_zero_list[k] > zero_list[k]):
                                        if total <= floor (n * m / 3):
                                            mylist[4] = j
                                            zero_list = cur_zero_list.copy()
                                            zero_list.append(j)
                                        break
                                    elif (cur_zero_list[k] < zero_list[k]):
                                        if total > floor (n * m / 3):
                                            mylist[4] = j
                                            zero_list = cur_zero_list.copy()
                                            zero_list.append(j)
                                        break

                            for k in range(4):
                                if cur_o_list[k] >= win_len:
                                    board[m - 1 - i][j] = 0
                                    return j
                                if (cur_o_list[k] > o_list[k]):
                                    cur_o_list.append(j)
                                    o_list = cur_o_list.copy()
                                    break
                                elif (cur_o_list[k] < o_list[k]):
                                    break
                        board[m - 1 - i][j] = 0
                        break
            if j + 1 >= n:
                j = 0
            else:
                j += 1
        if mylist[0] == -1:
            for count_times in range (n):
                if board[0][j] == 0:
                    for i in range (m):
                        if board[m - 1 - i][j] != 0:
                            continue
                        else:
                            board[m - 1 - i][j] = my_s
                            flag_test = True
                    
                            cur_list = find (board, m - 1 - i, j, m, n, my_s, win_len)
                            cur_zero_list = nonzero (board, m - 1 - i, j, m, n, my_s)
                            board[m - 1 - i][j] = my_s * 2
                            cur_o_list = opponent (board, m - 1 - i, j, m, n, my_s, win_len)
                            if flag == True:
                                if cur_zero_list[0] >= win_len:
                                    board[m - 1 - i][j] = 0
                                    return j
                                cur_list.append(j)
                                mylist = cur_list.copy()
                                cur_o_list.append(j)
                                o_list = cur_o_list.copy()
                                cur_zero_list.append(j)
                                zero_list = cur_zero_list.copy()
                                flag = False
                            else:
                                flag1 = True
                                for k in range(4):
                                    if (cur_list[k] > mylist[k]):
                                        cur_list.append(j)
                                        mylist = cur_list.copy()
                                        zero_list = cur_zero_list.copy()
                                        zero_list.append(j)
                                        flag1 = False
                                        break
                                    elif (cur_list[k] < mylist[k]):
                                        flag1 = False
                                        break
                                
                                if flag1 == True:
                                    for k in range(4):
                                        if (cur_zero_list[k] > zero_list[k]):
                                            mylist[4] = j
                                            zero_list = cur_zero_list.copy()
                                            zero_list.append(j)
                                            break
                                        elif (cur_zero_list[k] < zero_list[k]):
                                            break
                                    
                                for k in range(4):
                                    if (cur_o_list[k] > o_list[k]):
                                        cur_o_list.append(j)
                                        o_list = cur_o_list.copy()
                                        break
                                    elif (cur_o_list[k] < o_list[k]):
                                        break
                            board[m - 1 - i][j] = 0
                            break
                if j + 1 >= n:
                    j = 0
                else:
                    j += 1
                    
        for k in range(4):
            if o_list[k] > mylist[k] and o_list[k] >= win_len - 1 and total <= floor (n * m / 3):
                while board[0][o_list[4]] != 0:
                    o_list[4] += 1
                return o_list[4]
            elif (o_list[k] < mylist[k]):
                while board[0][mylist[4]] != 0:
                    mylist[4] += 1
                return mylist[4]
        while board[0][mylist[4]] != 0:
            mylist[4] += 1
        return mylist[4]
    
'''
mylist = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,'1',0,0]
]
agent = Agent ("Jim", '2',{"num_rows": 4,
    "num_cols": 6,
    "win_n": 3})
agent.get_move (mylist)
'''