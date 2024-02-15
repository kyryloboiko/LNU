'''
ui_template
┏━━━┳━━━┳━━━┓
┃ X │ O │ · ┃
┣───┼───┼───┫
┃ · │ X │ O ┃
┣───┼───┼───┫
┃ · │ · │ X ┃
┗━━━┻━━━┻━━━┛
'''
#Карта сітки (поле та значення в ньому) || Grid map (field and values in it)
map = {(0,0):'·',(0,1):'·',(0,2):'·',(1,0):'·',(1,1):'·',(1,2):'·',(2,0):'·',(2,1):'·',(2,2):'·'}

#Шаблон роздільних ліній сітки || Grid dividing lines template
top_game_lane = '┏━━━┳━━━┳━━━┓'
bottom_game_lane = '┗━━━┻━━━┻━━━┛'
middle_game_lane = '┣───┼───┼───┫'

#Шаблон відображення полів атрибутів || Attribute field display template
def attributes_game_lane(cell_a, cell_b, cell_c):
    result = '┃ ' + map.get(cell_a, ' ') + ' │ ' + map.get(cell_b, ' ') + ' │ ' + map.get(cell_c, ' ') + ' ┃'
    return result

#Відображення сітки гри || Displaying the game grid
def show_ui():
    print(top_game_lane)
    print(attributes_game_lane((0,0),(0,1),(0,2)))
    print(middle_game_lane)
    print(attributes_game_lane((1,0),(1,1),(1,2)))
    print(middle_game_lane)
    print(attributes_game_lane((2,0),(2,1),(2,2)))
    print(bottom_game_lane)

#Перевірка чи залишились пусті клітинки || Checking for empty cells
def draw_check():
    for value in map.values():
        if value == '·':
            return True
    return False

#Перевірка чи є переможні комбінації || Checking for winning combinations
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
        if map.get(i[0]) == map.get(i[1]) == map.get(i[2]) and map.get(i[0]) != '·':
            winner = map.get(i[0])
            print('Winner is ' + winner + '. Game over!')
            return False
    return True

#Хід хрестиків || Turn of the cross
def x_turn():
    input_cell_array = [int(i)
        for i in input("X turn, type row and column number across a space: ").split()]
    if map[(input_cell_array[0]-1,input_cell_array[1]-1)] == '·':
        x_append(input_cell_array[0]-1,input_cell_array[1]-1)
    else: 
        print('The cell is already occupied!!!')
        x_turn()

#Додавання хрестика в клітинку || Adding a cross to a cell
def x_append(row, column):
    if map[(row, column)] == '·':
        map[(row, column)] = 'X'

#Хід нуликів || Turn of the zero
def o_turn():
    input_cell_array = [int(i)
        for i in input("O turn, type row and column number across a space: ").split()]
    if map[(input_cell_array[0]-1,input_cell_array[1]-1)] == '·':
        o_append(input_cell_array[0]-1,input_cell_array[1]-1)
    else: 
        print('The cell is already occupied!!!')
        o_turn()
 
#Додавання нулика в клітинку || Adding a zero to a cell
def o_append(row, column):
    if map[(row, column)] == '·':
        map[(row, column)] = 'O'    

#Життєвий цикл гри || Game life cycle
game = True
while game == True:
    show_ui()
    game = win_check()
    if not game:
        break
    x_turn()
    show_ui()
    if not draw_check():
        print("Draw. Game over <3")
        break
    game = win_check()
    if not game:
        break
    o_turn()    