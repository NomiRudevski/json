from helper.functions import *
from enum import Enum

class Menu_actions(Enum):
    SHOW_ALL = 1
    ADD_NEW = 2
    UPDATE = 3
    DELETE = 4
    RESER_ALL = 5
    EXIT = 6

# array to exsecute on while program is running
cars = []


if __name__ == '__main__':
   cars = load_data_from_json('data.json')
   while True:
    print_all_actions(Menu_actions)
    user_selection = Menu_actions(validate_user_index_selection(Menu_actions) + 1)
    if user_selection == Menu_actions.SHOW_ALL: print_all_data_items(cars)
    if user_selection == Menu_actions.ADD_NEW: add_data_item(cars)
    if user_selection == Menu_actions.UPDATE: update_data_item(cars)
    if user_selection == Menu_actions.DELETE: delete_data_item(cars)
    if user_selection == Menu_actions.RESER_ALL: delete_all_data(cars, 'data.json')
    if user_selection == Menu_actions.EXIT: exit_and_save_app(cars, 'data.json')

