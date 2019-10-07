
def draw_borders(max_size, end_piece, start_piece):
    print("\t"+start_piece, end='')
    for i in range(0, max_size-1):
        print("-", end='')
    print(end_piece)


def find_max_column_length(table, title_list, column_index):
    length = len(title_list[column_index])
    for row in table:
        row_length = len(row[column_index])
        if row_length > length:
            length = row_length
    return length


def show_menu(options, exiting_message):
    for index, element in enumerate(options, 1):
        print(f"({index}) {element}")
    print(f"(0) {exiting_message}")


def get_input(label):
    input_ = input(label)
    return input_


def show_table(table, title_list):
    column_index = 0
    table_size = []
    for title in title_list:
        table_size.append(find_max_column_length(table, title_list, column_index))
        column_index += 1
    
    max_size = 0
    for size in table_size:
        max_size += size+3
    
    draw_borders(max_size, "/", "\\")

    print("\t|", end='')
    column_id = 0
    for title_column in title_list:
        print(title_column.center(table_size[column_id]+2, ' '), end='')
        print("|", end='')
        column_id += 1
    print("")

    for row in table:
        draw_borders(max_size, "|", "|")
        print("\t|", end='')
        column_id = 0
        for row_column in row:
            print(row_column.center(table_size[column_id]+2, ' '), end='')
            print("|", end='')
            column_id += 1
        print("")

    draw_borders(max_size, "\\", "/")
    print("")
