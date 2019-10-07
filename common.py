
def open_file(file_name):
    data = []
    with open(file_name, "r") as f:
        for line in f:
            data.append(line)
    return data
