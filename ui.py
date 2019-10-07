
def show_menu(options, exiting_message):
    for index, element in enumerate(options, 1):
        print(f"({index}) {element}")
    print(f"(0) {exiting_message}")


def get_inputs():
    label = "Choose option: "
    chosen_option = int(input(label))
    return chosen_option
