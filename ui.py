
def show_menu(options):
    for index, element in enumerate(options, 1):
        print(f"({index}) {element}")
    print("(0) Exit")


def get_inputs():
    label = "Choose option: "
    chosen_option = int(input(label))
    return chosen_option
