import sys
import ui
from entries import entries
import savings


def handle_menu():
    chosen_option = int(ui.get_input("Choose an option: "))
    if chosen_option == 1:
        entries.start_module()
    elif chosen_option == 2:
        savings.start_savings()
    elif chosen_option == 3:
        print("modul3")
    elif chosen_option == 0:
        sys.exit(0)
    else:
        raise KeyError("No such option")


def main():
    while True:
        options = ["Expense/Income", "Savings", "elem3"]
        ui.show_menu(options, "Exit")
        try:
            handle_menu()
        except KeyError as error:
            ui.print_message(str(error))


main()
