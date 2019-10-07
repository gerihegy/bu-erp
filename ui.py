import os


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu(options, exiting_message):
    clearscreen()
    for index, element in enumerate(options, 1):
        print(f"({index}) {element}")
    print(f"(0) {exiting_message}")
    print("\n")


def get_input(label):
    input_ = input(label)
    return input_


def draw_table_border(full_size, start, finish):
    print("\t"+start, end='')
    for i in range(0, full_size-1):
        print("-", end='')
    print(finish)


def find_max_column_length(table, title_list, column_index):
    length = len(title_list[column_index])
    for row in table:
        row_length = len(row[column_index])
        if row_length > length:
            length = row_length
    return length


def show_table(table, title_list):
    column_id = 0
    table_size = []
    for header in title_list:
        table_size.append(find_max_column_length(table, title_list, column_id))
        column_id += 1

    full_size = 0
    for size in table_size:
        full_size += size+3

    draw_table_border(full_size, "/", "\\")

    print("\t|", end='')
    column_id = 0
    for title_column in title_list:
        print(title_column.center(table_size[column_id]+2, ' '), end='')
        print("|", end='')
        column_id += 1
    print("")

    for row in table:
        draw_table_border(full_size, "|", "|")
        print("\t|", end='')
        column_id = 0
        for row_column in row:
            print(row_column.center(table_size[column_id]+2, ' '), end='')
            print("|", end='')
            column_id += 1
        print("")

    draw_table_border(full_size, "\\", "/")
    print("")


def print_message(message):
    print(message)
