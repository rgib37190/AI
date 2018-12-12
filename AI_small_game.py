import random
#開啟新遊戲
def new_board():
    return ['A',0,0,'B']
#呼叫new_board函數，讓玩家移動
def apply_move(board_state,move,side):
    action = move
    state_list = board_state
    if side == 'A':
        get_side_position = state_list.index('A')
    else:
        get_side_position = state_list.index('B')
    state_list[get_side_position] = 0 
    state_list[action] = side
    
    return state_list
#目前可以採取的行動
def available_moves(board_state,side):
    state_list = board_state
    current_position_A =  state_list.index('A')
    current_position_B = state_list.index('B')
    current_position0 = [i for i in range(len(state_list)) if state_list[i] == 0]
    if side == 'A':
        if current_position_A != 0:
            if state_list[current_position_A + 1] == 'B' or state_list[current_position_A - 1] == 'B':
                for available_move in current_position0:
                    if abs(current_position_B - available_move) <= 2:
                        yield available_move
            else:
                for available_move in current_position0:
                    yield available_move
        else:
            if state_list[current_position_A + 1] == 'B':
                for available_move in current_position0:
                    if abs(current_position_A - available_move) <=2:
                        yield available_move
            else:
                available_move = current_position_A + 1
                yield available_move
    elif side == 'B':
        if current_position_B != len(state_list) - 1 :
            if state_list[current_position_B + 1] == 'A' or state_list[current_position_B - 1] == 'A':
                for available_move in current_position0:
                    if abs(current_position_A - available_move) <= 2:
                        yield available_move
            else:
                for available_move in current_position0:
                    yield available_move
        else:
            if state_list[current_position_B - 1] == 'A':
                for available_move in current_position0:
                    if abs(current_position_B - available_move) <= 2:
                        yield available_move
            else:
                available_move = current_position_B -1
                yield available_move
#判斷贏家
def has_winner(board_state):
    if board_state[len(board_state) - 1] == 'A':
        return board_state[len(board_state) - 1]
    elif board_state[0] == 'B':
        return board_state[0]
    else:
        return 0
#開始遊戲(computer vs computer)
def play_game_by_computer(plus_player_func,minus_player_func):
    board_state = new_board()
    player_turn = 'A'
    time = 0
    while True:
        if player_turn == 'A':
            move = plus_player_func(board_state,'A')
        else:
            move = minus_player_func(board_state,'B')
        board_state = apply_move(board_state,move,player_turn)
        print(board_state)

        winner = has_winner(board_state)
        if winner != 0:
            print("we have a winner,side:%s" % player_turn)
            return winner
        if time % 2 == 1:
            player_turn = 'B'
        else:
            player_turn = 'A'
        time = time + 1 
#開始遊戲(human vs human)
def play_game_by_human():
    board_state = new_board()
    player = input('輸入玩家 A or B:')
    print(board_state)
    player_turn = player
    if player_turn == 'A':
        time = 0
    else:
        time = 1
    while True:
        if player_turn == 'A':
            print('A is your turn')
            available_move = list(available_moves(board_state,player_turn))
            print('The action you can do,move to:',[i+1 for i in available_move])
            error_condition = True
            while error_condition:
                try:
                    move = int(input('Your action:')) - 1
                    if move >= len(board_state) - 1:
                        print('You only enter available move number')
                    else:
                        error_condition = False
                except :
                    print('You only enter available move number')   
            time = time + 1
        else:
            print('B is your turn')
            available_move = list(available_moves(board_state,player_turn))
            print('The action you can do,move to:',[i+1 for i in available_move])
            try:
                move = int(input('Your action:')) - 1
            except:
                print('You only enter available move number')
                move = int(input('Your action:')) - 1
            time = time + 1
        board_state = apply_move(board_state,move,player_turn)
        print(board_state)

        winner = has_winner(board_state)
        if winner != 0:
            print("we have a winner,side:%s" % player_turn)
            return winner
        if time % 2 == 1:
            player_turn = 'B'
        else:
            player_turn = 'A'
#(computer vs computer)
def random_player(board_state,side):
    moves = list(available_moves(board_state,side))
    return random.choice(moves)

if __name__ == '__main__':
    play_game_by_human()

