import sys
import ui
from entries import entries
import savings


def handle_menu(chosen_option):
    while True:
        if chosen_option == 1:
            entries.start_module()
        elif chosen_option == 2:
            savings.start_savings()
        elif chosen_option == 3:
            print("modul3")
        elif chosen_option == 0:
            sys.exit(0)


def main():
    options = ["elem1", "Savings", "elem3"]
    ui.show_menu(options, "Exit")
    chosen_option = int(ui.get_input("Choose an option: "))
    handle_menu(chosen_option)


main()
