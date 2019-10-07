import ui

def savings_options(chosen_option):

    while True:
        if chosen_option == "1":
            show_savings()
        elif chosen_option == "2":
            add_pocket()
        elif chosen_option == "3":
            remove_pocket()
        elif chosen_option == "4":
            modify_pocket()
        elif chosen_option == "0":
            break

def start_savings():

    options = ["Show all savings", "Add new pocket", "Remove pocket", "Modify pocket"]
    ui.show_menu(options, "Back to main menu")

    chosen_option = ui.get_inputs("Please select an option: ")
    savings_options(chosen_option)