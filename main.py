
"""
 на 3 реализовать игру Угадай слово:
    - словарь из слов
    - рандомом выбирается слово
    - пользователю показывается '_' по количеству букв:
        для слова игра -> _ _ _ _

    - пользователь вводит букву -> она открывается
        для слова игра и буквы и -> И _ _ _
    - у пользователя ограниченное число попыток

на 4 игра крестики-нолики:
    - база:
        играют 2 игрока, первый нолик
        всегда выводится подсказка о том, как вводить новое значение:
        7 | 8 | 9
        --+---+--
        4 | 5 | 6
        --+---+--
        1 | 2 | 3

        пользователь вводит число и в ячейку ставится 'о' или 'х'
        после ввода крестика вводится нолик и наоборот
    - усложненный вариант:
        игра против компьютера, компьютер пытается победить

на 5 игра змейка:
    - задаётся размер игрового поля (10x10, 15x15, 20x20)
    - в центре появляется змейка размером 1 и в рандомной ячейке еда
    - при поглощении еды длина змейки увеличивается
    - пользователь вводит 'w', 'a' , 's', 'd' в ходе игры и поворачивает змейку
    - змейка не может врезаться в стенки и в себя

"""
import time

FIELD_CELL = '⬛'
SNAKE_CELL = '⬜'

FIELD_SIZE = 10

UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'


def generate_field(field_size):
    return [[FIELD_CELL for _ in range(field_size)]
             for _ in range(field_size)]

def clear_field():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def draw(field, field_size):
    for i in range(field_size):
        for j in range(field_size):
            print(field[i][j], end=' ')

        print()

def get_user_input(current_direction):
    import keyboard
    keys = [UP, DOWN, LEFT, RIGHT]
    for key in keys:
        if keyboard.is_pressed(key):
            return current_direction

    if keyboard.is_pressed('esc'):
        return 'exit'

DIRECTIONS = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1)
}

def change_field(field, current_direction, head, last_render):

    current_time = time.time()
    if last_render and current_time - last_render < 1:
        return head, last_render

    last_render = current_time

    head = (head[0] + DIRECTIONS[current_direction][0],
            head[1] + DIRECTIONS[current_direction][1])
    field[head[0]][head[1]] = SNAKE_CELL
    return head, last_render




if __name__ == '__main__':

    field = generate_field(FIELD_SIZE)

    current_direction = RIGHT
    head = (FIELD_SIZE//2, FIELD_SIZE//2)

    last_render = None
    while True:
        clear_field()
        get_user_input(current_direction)
        draw(field, FIELD_SIZE)
        head, last_render = change_field(field, current_direction, head, last_render)
        time.sleep(0.1)


