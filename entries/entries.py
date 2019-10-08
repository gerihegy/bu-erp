import ui
import common


def start_entry_module():
    while True:
        options = ["Record daily expense", "mennyit költöttem  idő alatt?"]
        ui.show_menu(options, "Back to main menu")
        try:
            chosen_option = int(ui.get_input("Please select an option: "))
            if chosen_option == 1:
                declare_expense_or_income()
            elif chosen_option == 0:
                break
            else:
                raise KeyError("No such option")
        except KeyError as error:
            ui.print_message(str(error))


def declare_expense_or_income():

    ui.clearscreen()

    expense_list = []
    path = "entries/entries.csv"

    day = ui.get_input("Please specify the day:" + "\n")
    month = ui.get_input("Please specify the month:" + "\n")
    year = ui.get_input("Please specify the year:" + "\n")
    date = ".".join([day, month, year])

    in_out = ui.get_input("Was it an income or an expense:" + "\n")
    cost = ui.get_input("Specify the amount" + "\n")
    category = ui.get_input("What category of expense was it?" + "\n")
    expense_list.append([in_out, date, cost, category])

    print(f'\nType: {in_out} date: {date} the cost is {cost}, and the category is: {category}')
    common.append_to_file(path, expense_list)

    input("\nPress any key to continue")
