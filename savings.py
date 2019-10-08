import ui
import common


def show_savings():

    ui.clearscreen()
    pockets = common.open_file("pockets.csv")
    title_list = ["Pocket", "Amount"]

    if pockets == "File doesn't exist":
        ui.print_message("You doesn't have any savings yet.")
    else:
        ui.show_table(pockets, title_list)

    input("Press any key to continue: ")


def add_pocket():

    ui.clearscreen()
    pockets = common.open_file("pockets.csv")
    if pockets == "File doesn't exist":
        pockets = []

    ui.print_message("Add a new pocket\n")
    new_pocket_name = ui.get_input("Pocket's name: ")
    new_pocket_amount = ui.get_input("Pocket's amount: ")

    pockets.append([new_pocket_name, new_pocket_amount])

    common.write_to_file("pockets.csv", pockets)


def remove_pocket():

    ui.clearscreen()
    pockets = common.open_file("pockets.csv")

    if pockets == "File doesn't exist":
        ui.print_message("You doesn't have any savings yet.")

    else:
        pocket_name = ui.get_input("Pocket's name: ")
        name = 0
        for pocket in pockets:
            if pocket[name] == pocket_name:
                pockets.remove(pocket)
        common.write_to_file("pockets.csv", pockets)


def modify_pocket():

    ui.clearscreen()
    pockets = common.open_file("pockets.csv")

    if pockets == "File doesn't exist":
        ui.print_message("You doesn't have any savings yet.")

    else:
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


def start_savings():

    ui.clearscreen()
    options = ["Show all savings", "Add new pocket", "Remove pocket", "Modify pocket"]

    while True:
        ui.show_menu(options, "Back to main menu")
        try:
            chosen_option = int(ui.get_input("Please select an option: "))
            if chosen_option == 1:
                show_savings()
            elif chosen_option == 2:
                add_pocket()
            elif chosen_option == 3:
                remove_pocket()
            elif chosen_option == 4:
                modify_pocket()
            elif chosen_option == 0:
                break
            else:
                raise KeyError("No such option")
        except KeyError as error:
            ui.print_message(str(error))
