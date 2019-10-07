import ui
import common


def add_pocket():

    pockets = common.open_file("pockets.csv")

    new_pocket_name = ui.get_input("Pocket's name: ")
    new_pocket_amount = int(ui.get_input("Pocket's amount: "))

    pockets.append([new_pocket_name, new_pocket_amount])

    common.write_to_file("pockets.csv", pockets)


def remove_pocket():

    pockets = common.open_file("pockets.csv")

    pocket_name = ui.get_input("Pocket's name: ")

    name = 0
    for pocket in pockets:
        if pocket[name] == pocket_name:
            pockets.remove(pocket)

    common.write_to_file("pockets.csv", pockets)


def modify_pocket():

    pockets = common.open_file("pockets.csv")

    modify = ui.get_input("Pocket's name: ")
    pocket_name = ui.get_input("Pocket's new name: ")
    pocket_amount = int(ui.get_input("Pocket's new amount: "))

    found_name = False
    name = 0
    amount = 1
    for pocket in pockets:
        if pocket[name] == modify:
            pocket[name] = pocket_name
            pocket[amount] = pocket_amount
            found_name = True

    if found_name is False:
        ui.print_message("Pocket is not found")


def savings_options(chosen_option):

    while True:
        if chosen_option == "1":
            title_list = ["Name", "Amount"]
            table = common.open_file("pocets.csv")
            ui.show_table(table, title_list)
        elif chosen_option == "2":
            add_pocket()
        elif chosen_option == 3:
            remove_pocket()
        elif chosen_option == 4:
            modify_pocket()
        elif chosen_option == 0:
            break


def start_savings():

    options = ["Show all savings", "Add new pocket", "Remove pocket", "Modify pocket"]
    ui.show_menu(options, "Back to main menu")

    chosen_option = int(ui.get_input("Please select an option: "))
    savings_options(chosen_option)
