import ui
import common



def start_module():
    ui.clearscreen()
    expense_list = common.open_file("entries/entries.csv")
    cost = ui.get_input("What was your last transaction?")
    category = ui.get_input("What category of expense was it?")
    print(f'the cost is {cost}, and the cat is:{category}')
    expense_list.append([cost, category])
    common.write_to_file("entries.csv", expense_list)

    input()


        