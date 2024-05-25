initialState = '-'
def printGrid():
    for row in G:
        for col in row:
            print(col, end='  ')
        print()
    print('------------------------------')
def checkWinner():
    if G[0][0] != '-':
        if G[0][0] == G[0][1] and G[0][0] == G[0][2]:
            return True
        elif G[0][0] == G[1][0] and G[0][0] == G[2][0]:
            return True
        elif G[0][0] == G[1][1] and G[0][0] == G[2][2]:
            return True
    if G[1][0] != initialState and G[1][0] == G[1][1] and G[1][0] == G[1][2]:
        return True
    if G[2][0] != initialState:
        if G[2][0] == G[2][1] and G[2][0] == G[2][2]:
            return True
        elif G[2][0] == G[1][1] and G[2][0] == G[0][2]:
            return True
    if G[0][1] != initialState and G[0][1] == G[1][1] and G[0][1] == G[2][1]:
        return True
    if G[0][2] != initialState and G[0][2] == G[1][2] and G[0][2] == G[2][2]:
        return True
    return False

G = [['-']*3 for _ in range(3)]

while True:
    printGrid()
    x, y = map(int, input('Input coordinate (integers) 0-3: ').split())
    print(f'your input is {x} and {y}')
    c = input('Enter your symbols: ')
    G[x][y] = c
    printGrid()
    print('Checking Grid')
    if checkWinner() == True:
        print(f'{c} wins')
        break
    else:
        print(f'No winner yet')

