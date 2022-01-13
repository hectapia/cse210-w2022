"""
TicTacToe game by Hector Olivares Tapia
Handling Exceptions are included
CSE 210 | Programming With Classes
Brigham Young University - Idaho

"""

grid_positions = [1,2,3,4,5,6,7,8,9]
grid_inputs = []
turns = ['X','O']
xos = []
grid_board = ['E0','E1','E2','E3','E4','E5','E6','E7','E8','E9']
get_winner = [0,1,2,3,4,5,6,7,8,0,4,8,0,3,6,1,4,7,2,5,8,2,4,6,0]


def main():
    print('\n\033[1;37;41m   TIC-TAC-TOE  \033[0m\n')
    position(0,'',0)
    turn = 0
    xo = 0
    while turn != 9 :
        try:
            print(f"\033[1;37;45m {turns[xo]}'s turn to choose a square (1-9): \033[0m",end='')
            grid_posi = int(input(" "))

            if grid_posi in grid_inputs:
                print('turn is already occupied')
            elif grid_posi < 1 or grid_posi > 9:
                print('choose a square (1-9)')
            else:
                print()
                print('\n\033[1;37;41m   TIC-TAC-TOE  \033[0m\n')
                signal = position(grid_posi, turns[xo], xo)
                if signal == 1 : 
                    print('\n\033[1;37;41m Good game. Thanks for playing \033[0m\n')
                    break
                turn += 1
                xo += 1
                if xo == 2 : xo = 0
        except ValueError as val_err:
            print(val_err)

def position(grid_pos, v, xo):
    signal = 0
    if grid_pos != 0 : 
        grid_inputs.append(grid_pos)
        xos.append(v)
    k = 0
    m = 0
    for i in range(3):
        for j in range(3):
            k += 1
            if k == 3 or k == 6 or k == 9: 
                if grid_pos == k : print(f'\033[1;37;44m {v} \033[0m\033[0;30;47m \033[0m', end='')
                else : 
                    if (k in grid_inputs)  :
                        n = grid_inputs.index(k)
                        print(f'\033[1;37;44m {xos[n]} \033[0m\033[0;30;47m \033[0m', end='')  
                    else :
                         print(f'\033[1;37;44m {(k)} \033[0m\033[0;30;47m \033[0m', end='')         
            else:  
                if grid_pos == k : print(f'\033[1;37;44m {v} \033[0m\033[0;30;47m | \033[0m', end='')
                else :  
                    if (k in grid_inputs)  :
                        n = grid_inputs.index(k)
                        print(f'\033[1;37;44m {xos[n]} \033[0m\033[0;30;47m | \033[0m', end='')
                    else :    
                        print(f'\033[1;37;44m {(k)} \033[0m\033[0;30;47m | \033[0m', end='')
            m += 1            
        print()
        if k < 7 : 
            for l in range(8): print(f'\033[0;30;47m--\033[0m',end='')
        print()
    signal = verify_winner(signal)
    return signal

def verify_winner(signal):
    for i in range(len(grid_inputs)):
        grid_board[grid_inputs[i]-1] = xos[i]
    
    i = 0
    j = 0
    k = 0
    l = 0
    while i <= 23:
        while j <= 2:
            if grid_board[get_winner[i]] == 'X':
                k += 1
                if k == 3 : 
                    print('\033[1;30;47m  <<<<<< Y O U   W I N >>>>>>  \033[0m\n')
                    signal = 1  
            if grid_board[get_winner[i]] == 'O': 
                l += 1
                if l == 3 : 
                    print('\033[1;30;47m  <<<<<< Y O U   W I N >>>>>>  \033[0m\n') 
                    signal = 1  
            j +=1
            i +=1

        j = 0
        k = 0
        l = 0
    return signal

if __name__ == "__main__":
    main()