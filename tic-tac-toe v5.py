cells = [' ' for i in range(0,9)]
allowed_coordinates = [['1', '3'], ['2', '3'], ['3', '3'],
                ['1', '2'], ['2', '2'], ['3', '2'],
                ['1', '1'], ['2', '1'], ['3', '1']]
win_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
              [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
cell = 'X'


def switch(turn):
    global cell
    if turn % 2:
        cell = 'O'
    else:
        cell = 'X'


def box():
    global cells
    print('---------')
    for i in range(0, 9, 3):
        print('|', *cells[i:i + 3], '|')
    print('---------')


def player_move():
    global allowed_coordinates, cells, cell
    turn = 0
    # to prevent changing cell's turn by wrong input
    move = False
    while True:
        box()
        if check():
            print(f'☝( ◠‿◠ )☝ {cell} WINS ☝( ◠‿◠ )☝')
            break
        if move:
            turn += 1
            switch(turn)
        if turn == 9:
            print('wat,\n'
                  'Draw (ノ^_^)ノ')
            break

        coordinates = input().split()

        if coordinates in allowed_coordinates:
            if coordinates[1] == '3':
                if cells[int(coordinates[0]) - 1] == ' ':
                    cells[int(coordinates[0]) - 1] = cell
                    move = True
                else:
                    print('"This cell is occupied! Choose another one!"')
                    move = False
            elif coordinates[1] == '2':
                if cells[int(coordinates[0]) + 2] == ' ':
                    cells[int(coordinates[0]) + 2] = cell
                    move = True
                else:
                    print('"This cell is occupied! Choose another one!"')
                    move = False
            else:
                if cells[int(coordinates[0]) + 5] == ' ':
                    cells[int(coordinates[0]) + 5] = cell
                    move = True
                else:
                    print('"This cell is occupied! Choose another one!"')
                    move = False

        elif coordinates[0].isdigit() and coordinates[1].isdigit():
            print("Coordinates should be from 1 to 3!")
            move = False
        else:
            print("You should enter numbers!")
            move = False


def check():
    global cell, win_states, cells
    proc = [i for i in range(9) if cells[i] == cell]
    for state in win_states:
        if all(key in proc for key in state):
            return 1


player_move()