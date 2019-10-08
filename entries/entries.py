import ui
import common


def start_module():
    ui.clearscreen()
    expense_list = []
    path = "entries/entries.csv"
    date = ui.get_input("Please specify the date:" + "\n")
    cost = ui.get_input("What was your last transaction?" + "\n")
    category = ui.get_input("What category of expense was it?" + "\n")
    expense_list.append([date, cost, category])
    print(f'Date:{date} the cost is {cost}, and the cat is:{category}')
    common.append_to_file(path, expense_list)

    input("Press any key to continue")
