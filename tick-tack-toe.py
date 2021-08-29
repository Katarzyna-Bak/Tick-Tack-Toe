def draw(field):
    for row in range(5):
        if row % 2 == 0:
            correctedRow = int(row / 2)
            for column in range(5):
                if column % 2 == 0:
                    correctedColumn = int(column / 2)
                    if column != 4:
                        print(field[correctedColumn][correctedRow], end="")
                    else:
                        print(field[correctedColumn][correctedRow])
                else:
                    print('|', end="")
        else:
            print('-----')

player = 1
currentField = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

while(True):
    print('Player {} turn!'.format(player))
    moveRow = int(input('Please enter the row: '))-1
    moveColumn = int(input('Please enter the column: '))-1
    if player == 1:
        if currentField[moveColumn][moveRow] == ' ':
            currentField[moveColumn][moveRow] = 'X'
            player = 2
    else:
        if currentField[moveColumn][moveRow] == ' ':
            currentField[moveColumn][moveRow] = 'O' 
            player = 1      
    draw(currentField)