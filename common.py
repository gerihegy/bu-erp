
def open_file(file_name):
    data = []
    with open(file_name, "r") as f:
        for line in f:
            data.append(line.split(","))
    return data


def write_to_file(file_name, table):
    with open(file_name, "w") as f:
        for data in table:
            for item in data:
                row = "," + str(item)
                f.write(row + "\n")
