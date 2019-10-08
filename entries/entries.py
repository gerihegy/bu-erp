import ui
import common


def start_module():
    ui.clearscreen()
    expense_list = []
    path = "entries/entries.csv"
    date = ui.get_input("Please specify the date:" + "\n")
    in_out = ui.get_input("Was it an income or an expense:" + "\n")
    cost = ui.get_input("How much was your last transaction" + "\n")
    category = ui.get_input("What category of expense was it?" + "\n")
    expense_list.append([in_out, date, cost, category])
    print(f'Type: {in_out} date:{date} the cost is {cost}, and the category is:{category}')
    common.append_to_file(path, expense_list)

    input("Press any key to continue")
