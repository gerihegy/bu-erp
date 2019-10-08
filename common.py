import os


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
