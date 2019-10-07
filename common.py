
def open_file(file_name):
    data = []
    with open(file_name, "r") as f:
        for line in f:
            line = line[:-1]
            data.append(line.split(","))
    return data


def write_to_file(file_name, table):
    with open(file_name, "w") as f:
        for data in table:
            row = ",".join(str(data))
            f.write(row + "\n")

