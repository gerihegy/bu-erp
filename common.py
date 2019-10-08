import os
import ui


def open_file(file_name):
    if os.path.exists(file_name):
        data = []
        with open(file_name, "r") as f:
            for line in f:
                line = line[:-1]
                data.append(line.split(";"))
        return data
    else:
        return "File doesn't exist"


def write_to_file(file_name, table):
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def append_to_file(file_name, table):
    with open(file_name, "a") as file:
        for record in table:
            row = ";".join(record)
            file.write(row + "\n")


def sum_column(table, column):

    sum_ = 0
    for row in table:
        sum_ += int(row[column])

    return sum_


def remove_row(input_file, output_file, row_name):

    ui.clearscreen()
    list_ = open_file(input_file)

    if list_ == "File doesn't exist":
        ui.print_message("File doesn't exist")

    else:
        input_ = ui.get_input(f"{row_name}'s name: ")
        name = 0
        found_row_name = False
        for row in list_:
            if row[name] == input_:
                list_.remove(row)
                found_row_name = True
        if found_row_name:
            write_to_file(output_file, list_)
        else:
            ui.print_message(f"\n{row_name} is not found")
