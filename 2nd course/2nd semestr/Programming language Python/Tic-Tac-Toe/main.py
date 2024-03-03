'''
ui_template
┏━━━┳━━━┳━━━┓
┃ X │ O │   ┃
┣───┼───┼───┫
┃   │ X │ O ┃
┣───┼───┼───┫
┃   │   │ X ┃
┗━━━┻━━━┻━━━┛
'''
#Карта сітки (поле та значення в ньому) || Grid map (field and values in it)
void_attribute = ' '
map = {(row, col): void_attribute for row in range(3) for col in range(3)}

#Шаблон роздільних ліній сітки || Grid dividing lines template
top_game_lane = '┏━━━┳━━━┳━━━┓'
bottom_game_lane = '┗━━━┻━━━┻━━━┛'
middle_game_lane = '┣───┼───┼───┫'

#Шаблон відображення полів атрибутів || Attribute field display template
def attributes_game_lane(cell_a, cell_b, cell_c):
    return f'┃ {map.get(cell_a, void_attribute)} │ {map.get(cell_b, void_attribute)} │ {map.get(cell_c, void_attribute)} ┃'

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
    return any(value == void_attribute for value in map.values())

#Перевірка чи є переможні комбінації || Checking for winning combinations
def win_check():
    for row in range(3):
        if map[(row, 0)] == map[(row, 1)] == map[(row, 2)] != void_attribute:
            print(f'Winner is {map[(row, 0)]}. Game over!')
            return False
        if map[(0, row)] == map[(1, row)] == map[(2, row)] != void_attribute:
            print(f'Winner is {map[(0, row)]}. Game over!')
            return False
    if map[(0, 0)] == map[(1, 1)] == map[(2, 2)] != void_attribute or map[(0, 2)] == map[(1, 1)] == map[(2, 0)] != void_attribute:
        print(f'Winner is {map[(1, 1)]}. Game over!')
        return False
    return True

#Хід гравця || Player turn
def player_turn(player):
    input_cell_array = [int(i) for i in input(f"{player} turn, type row and column number across a space: ").split()]
    while len(input_cell_array) != 2 or map[(input_cell_array[0]-1, input_cell_array[1]-1)] != void_attribute:
        print('Invalid input or cell is already occupied!!!')
        input_cell_array = [int(i) for i in input(f"{player} turn, type row and column number across a space: ").split()]
    map[(input_cell_array[0]-1, input_cell_array[1]-1)] = player

#Додавання значення в клітинку || Adding sense to a cell
def append_to_cell(row, column, player):
    map[(row, column)] = player

#Життєвий цикл гри || Game life cycle
game = True
while game:
    show_ui()
    game = win_check()
    if not game:
        break
    player_turn('X')
    show_ui()
    if not draw_check():
        print("Draw. Game over <3")
        break
    game = win_check()
    if not game:
        break
    player_turn('O')
