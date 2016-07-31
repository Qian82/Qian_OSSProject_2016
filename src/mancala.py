# Copyright (c) 2016 Qian Song
# This program is available under MIT licence, please see COPYING.
# Mancala Game for OSS summer project



import sys
import copy

MAX_VALUE = 1000000
MIN_VALUE = -1000000


def evaluation(): # whose mancala has more stones
    global A, B, Player
    if Player == 1:
        return B[-1] - A[1]
    else:
        return A[1] - B[-1]


def add_one(mark, i, player): #calculate which pit to add one for the next time, call this function n times if #there are n stones in the chosen pit
    global A, B
    if mark == 1:  # current pit is B's plate
        if i <= len(A)-2:
            return mark, i+1
        elif i == len(A)-1:
            if player == 1:
                return mark, i+1  # first parameter gives which plate, second prameter gives which pit
            else:
                return 3-mark, len(A)-1
        else:
            return 3-mark, len(A)-1
    else:
        if i >= 3:
            return mark, i-1
        elif i == 2:
            if player == 2:
                return mark, i-1
            else:
                return 3-mark, 2
        else:
            return 3-mark, 2


def end_game():
    global A, B
    a_mark = True
    b_mark = True
    for i in A[2:]:
        if i != 0:
            a_mark = False
    for i in B[2:-1]:
        if i != 0:
            b_mark = False
    return a_mark or b_mark


def clear_game():
    for i in range(2, len(A)):
        A[1] += A[i]
        A[i] = 0
    for i in range(2, len(A)):
        B[len(A)] += B[i]
        B[i] = 0


def move(player, i):  # player=1 : B move; player = 2: A move; i represents which pit in the player's plate
    global A, B
    if player == 1:
        _sum = B[i]   #sum is # of stones in the chosen pit
        B[i] = 0
    else:
        _sum = A[i]
        A[i] = 0
    if _sum == 0:
        return False
    mark = player
    while _sum:
        mark, i = add_one(mark, i, player)
        _sum -= 1
        if mark == 1:
            B[i] += 1
        else:
            A[i] += 1
    if end_game():
        clear_game()
        return False  # last stone just in self's mancala, can move one more step
    if mark != player:
        return False
    else:
        if i == 1 or i == len(A):# last stone just in self's mancala, can move one more step
            return True
        if mark == 1 and B[i] == 1: # last stone just in self's empty pit, eat corresponding stone in others pit
            B[len(A)] += B[i] + A[i]
            B[i] = 0
            A[i] = 0
        if mark == 2 and A[i] == 1:
            A[1] += A[i] + B[i]
            A[i] = 0
            B[i] = 0
        if end_game():
            clear_game()
        return False


def greedy():
    global A, B, Player, Max, Result_A, Result_B
    for i in range(2, len(A)):
        if Player == 1 and B[i] == 0:
            continue
        if Player == 2 and A[i] == 0:
            continue
        _A = copy.copy(A)
        _B = copy.copy(B)
        move_again = move(Player, i)
        if move_again:
            greedy()
        elif evaluation() > Max:
            Max = evaluation()
            Result_A = copy.copy(A)
            Result_B = copy.copy(B)
        A = _A
        B = _B


def output_f1():
    for i in Result_A[2:]:
        output_file1.write(str(i))
        output_file1.write(' ')
    output_file1.write('\n')
    for i in Result_B[2:-1]:
        output_file1.write(str(i))
        output_file1.write(' ')
    output_file1.write('\n')
    if len(Result_A) < 3:
        return
    output_file1.write(str(Result_A[1]))
    output_file1.write('\n')
    output_file1.write(str(Result_B[-1]))
    output_file1.write('\n')


def min_value(depth, player, prev_player, position):
    global A, B, Depth_max #how many steps to consider
    if end_game() or depth == Depth_max:
        return evaluation()
    min_eval = MAX_VALUE
    for i in range(2, len(A)):
        if player == 1 and B[i] == 0:
            continue
        if player == 2 and A[i] == 0:
            continue
        _A = copy.copy(A)
        _B = copy.copy(B)
        move_again = move(player, i)
        if end_game():
            clear_game()
            _temp = evaluation()
            #output(player, i, depth+1, _temp)
        elif move_again:
            #output(player, i, depth+1, MAX_VALUE)
            _temp = min_value(depth, player, player, i)
        elif depth+1 == Depth_max:
            _temp = evaluation()
            #output(player, i, depth+1, _temp)
        else:
            #output(player, i, depth+1, MIN_VALUE)
            _temp = max_value(depth+1, 3-player, player, i)
        if min_eval > _temp:
            min_eval = _temp
        A = _A
        B = _B
    return min_eval


def max_value(depth, player, prev_player, position):
    global A, B, Depth_max
    if end_game() or depth == Depth_max:
        return evaluation()
    max_eval = MIN_VALUE
    for i in range(2, len(A)):
        if player == 1 and B[i] == 0:
            continue
        if player == 2 and A[i] == 0:
            continue
        _A = copy.copy(A)
        _B = copy.copy(B)
        move_again = move(player, i)
        if end_game():
            clear_game()
            _temp = evaluation()
        elif move_again:
            _temp = max_value(depth, player, player, i)
        elif depth+1 == Depth_max:
            _temp = evaluation()
        else:
            _temp = min_value(depth+1, 3-player, player, i)
        if max_eval < _temp:
            max_eval = _temp
        A = _A
        B = _B
    return max_eval


def minimax_decision(depth=0, position = 2): #
    global A, B, Player, Max, Result_A, Result_B

    max_eval = MIN_VALUE
    for i in range(2, len(A)):
        if Player == 1 and B[i] == 0:
            continue
        if Player == 2 and A[i] == 0:
            continue
        _A = copy.copy(A)
        _B = copy.copy(B)
        move_again = move(Player, i)
        if end_game():
            clear_game()
            _temp = evaluation()
        elif move_again:
            _temp = minimax_decision(1, i)
        elif Depth_max == 1:
            _temp = evaluation()
        else:
            _temp = min_value(1, 3-Player, Player, i)
        if max_eval < _temp:
            max_eval = _temp
        if Max < _temp:
            Max = _temp
            Result_A = copy.copy(A)
            Result_B = copy.copy(B)
        A = _A
        B = _B
    return max_eval


Max = MIN_VALUE
Result_A = []
Result_B = []
#Opt = []


def init():
    global A, B, Player, Algorithm, Depth_max
    Player = 2
    Algorithm = 2
    Depth_max = 5
    A = [0, 0, 4, 4, 4, 4, 4, 4]
    B = [0, 0, 4, 4, 4, 4, 4, 4, 0]


def print_mancala():
    print A
    print B


def pvp():
    global A, B
    while True: # a b take turns
        while True: #b move
            print_mancala()
            while True:# player input until it is legal
                i = raw_input('Player B:') # input string
                if len(i) != 1 or not (i>='2' and i<='7'):
                    print 'Input is wrong!'
                elif B[int(i)] == 0: # pit is empty, illegal
                    print 'It is empty!'
                else:
                    break
            move_again = move(1, int(i))
            if not move_again:
                break
        if end_game():
            break
        while True: #a move
            print_mancala()
            while True:
                i = raw_input('Player A:')
                if len(i) != 1 or not (i>='2' and i<='7'):
                    print 'Input is wrong!'
                elif A[int(i)] == 0:
                    print 'It is empty!'
                else:
                    break
            move_again = move(2, int(i))
            if not move_again:
                break
        if end_game():
            break
    print 'The final is:'
    print_mancala()
    if (evaluation() > 0):
        print 'B Wins!'
    elif (evaluation() < 0):
        print 'A Wins!'
    else:
        print 'Ties!'


def pvc():
    global A, B, Max, Result_A, Result_B, Opt
    while True:
        while True:#player
            print_mancala()
            while True:#if legal or not
                i = raw_input('Player B:')
                if len(i) != 1 or not (i>='2' and i<='7'):
                    print 'Input is wrong!'
                elif B[int(i)] == 0:
                    print 'It is empty!'
                else:
                    break # jump out of third while
            move_again = move(1, int(i)) # return boolean value if it can move again
            if not move_again:
                break # jump outof second while
        if end_game():
            break #jump out of first while
        print_mancala() # print plate state
        print 'Computer Plays:'
        Max = MIN_VALUE
        Result_A = []
        Result_B = []
        # Opt = []
        minimax_decision()
        A = copy.copy(Result_A)
        B = copy.copy(Result_B)
        if end_game():
            break
    print 'The final is:'
    print_mancala()
    if (evaluation() < 0):
        print 'B Wins!'
    elif (evaluation() > 0):
        print 'A Wins!'
    else:
        print 'Ties!'


while True:
    init()
    print 'Welcome to mancala!'
    print 'Please choose:'
    print '1. Play with Player.'
    print '2. Play with Computer'
    print '3. Quit Game!'
    choose = raw_input()
    if choose == '1':
        pvp()
        print 'You have finished. See You!'
        break
    elif choose == '2':
        pvc()
        print 'You have finished. See You!'
        break
    elif choose == '3':
        print 'See You!'
        break
    else:
        print 'Input is Wrong, Please Input again!'



