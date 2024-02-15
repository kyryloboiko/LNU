'''
┏━━━┳━━━┳━━━┓
┃ X │ O │ · ┃
┣───┼───┼───┫
┃ · │ X │ O ┃
┣───┼───┼───┫
┃ · │ · │ X ┃
┗━━━┻━━━┻━━━┛
'''
#Карта сітки (поле та значення в ньому)
map = {(0,0):'·',(0,1):'·',(0,2):'·',(1,0):'·',(1,1):'·',(1,2):'·',(2,0):'·',(2,1):'·',(2,2):'·'}

#Шаблон роздільних ліній сітки
top_game_lane = '┏━━━┳━━━┳━━━┓'
bottom_game_lane = '┗━━━┻━━━┻━━━┛'
middle_game_lane = '┣───┼───┼───┫'

#Шаблон відображення полів атрибутів
def attributes_game_lane(cell_a, cell_b, cell_c):
    result = '┃ ' + map.get(cell_a, ' ') + ' │ ' + map.get(cell_b, ' ') + ' │ ' + map.get(cell_c, ' ') + ' ┃'
    return result

#Відображення сітки гри
def show_ui():
    print(top_game_lane)
    print(attributes_game_lane((0,0),(0,1),(0,2)))
    print(middle_game_lane)
    print(attributes_game_lane((1,0),(1,1),(1,2)))
    print(middle_game_lane)
    print(attributes_game_lane((2,0),(2,1),(2,2)))
    print(bottom_game_lane)
    
def win_check():
    winning_combinations = [[(0,0),(0,1),(0,2)],
                            [(1,0),(1,1),(1,2)],
                            [(2,0),(2,1),(2,2)],
                            [(0,0),(1,0),(2,0)],
                            [(0,1),(1,1),(2,1)],
                            [(0,2),(1,2),(2,2)],
                            [(0,0),(1,1),(2,2)],
                            [(0,2),(1,1),(2,0)]]
    for i in winning_combinations:
        if map.get(i[0]) == map.get(i[1]) == map.get(i[2]) == 'X' or map.get(i[0]) == map.get(i[1]) == map.get(i[2]) == 'O':
            winner = map.get(i[0])
            print('Winner is ' + winner)
            return False

def x_append(row, column):
    if map[(row, column)] == '·':
        map[(row, column)] = 'X'

def o_append(row, column):
    if map[(row, column)] == '·':
        map[(row, column)] = 'O'    

game = True
while game == True:
    show_ui()
    game = win_check()
    input_cell_array = [int(i)
        for i in input("X turn, type row and column number across a space: ").split()]
    x_append(input_cell_array[0]-1,input_cell_array[1]-1)
    show_ui()
    game = win_check()
    input_cell_array = [int(i)
        for i in input("O turn, type row and column number across a space: ").split()]
    o_append(input_cell_array[0]-1,input_cell_array[1]-1)