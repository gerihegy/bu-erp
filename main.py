import sys
import ui
from entries import entries
import savings


def handle_menu():
    chosen_option = int(ui.get_input("Choose an option: "))
    if chosen_option == 1:
        entries.start_entry_module()
    elif chosen_option == 2:
        savings.start_savings()
    elif chosen_option == 3:
        print("This will be Modul3")
    elif chosen_option == 0:
        sys.exit(0)
    else:
        raise KeyError("No such option")


def main():
    while True:
        options = ["Income/Expense", "Savings", "Monthly review"]
        ui.show_menu(options, "Exit")
        try:
            handle_menu()
        except KeyError as error:
            ui.print_message(str(error))


main()
