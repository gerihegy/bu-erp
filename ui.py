
def show_menu(options, exiting_message):
    for index, element in enumerate(options, 1):
        print(f"({index}) {element}")
    print(f"(0) {exiting_message}")


def get_input(label):
    input_ = input(label)
    return input_
