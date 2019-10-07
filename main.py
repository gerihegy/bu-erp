import sys
import ui


def handle_menu(chosen_option):
    while True:
        if chosen_option == 1:
            print("modul1")
        elif chosen_option == 2:
            print("modul2")
        elif chosen_option == 3:
            print("modul3")
        elif chosen_option == 0:
            sys.exit(0)


def main():
    options = ["elem1", "elem2", "elem3"]
    ui.show_menu(options, "Exit")
    chosen_option = ui.get_inputs()
    handle_menu(chosen_option)


main()
