import json
from print_color import print
from enum import Enum

class Car():    
    def __init__(self, color, brand, custumer) -> None:
        self.color = color
        self.brand = brand
        self.costumer = custumer

    def __str__(self) -> str:
        return f'color: {self.color}, brand: {self.brand}, custumer name: {self.costumer}'
    
    def as_dict(self) -> dict:
        return{
            "color" : self.color,
            "brand" : self.brand,
            "custumer" : self.costumer
        }

def print_all_actions(array):
    for action in array:
        print(f'{action.value} - {action.name}', color='cyan')

def validate_user_index_selection(array):
    while True:
        user_input = input("Choose an option number: ")
        try:
            user_input = int(user_input)-1
            if 0 <= user_input < len(array):
                return user_input
            else:
                print('Input is invalid!', color='red')
        except:
            print('Input is invalid!', color='red')

def print_all_data_items(array):
    if array == []: return print ("No options available", color='red')
    for i, item in enumerate(array):
        print(f'{i+1} - {item}', color='yan')

def get_item_from_user():
    item = Car(input("What is the color of the car?"),input("What is the brand of the car?"),input("what is the custumer's name? "))
    return item

def update_data_item(array):
    if array == [] : return print ("No options available", color='red')
    print_all_data_items(array)
    index = validate_user_index_selection(array)
    item = get_item_from_user()
    array[index] = item
    print('item added successfuly!', color='green')

def add_data_item(array):
    print("please enter the needed ditailes:", color= "yellow")
    item = get_item_from_user()
    array.append(item)
    print('Item added successfuly!', color='green')

def delete_data_item(array):
    if array == [] : return print ("No options available", color='red')
    print_all_data_items(array)
    index = validate_user_index_selection(array)
    print("Item removed successfuly!", color='green')
    array.pop(index)

def action_comfirmation():
     print("Are you sure you want to commit this action?", color='red')
     while True:
        print ("Please enter y/n:", color='yellow')
        user_input = input()
        if user_input.lower() == 'y' :
            print('Action will be excecuted', color='yellow')
            return True
        elif user_input.lower() == 'n':
            print('Action was canceled', color='yellow')
            return False
        else:
            print("input invalid", color='red')
        
def delete_all_data(array, DB_file_name):
    array
    if action_comfirmation():
        array.clear()
        with open(DB_file_name, 'w') as file:
            json.dump([], file)
    else: return

def exit_and_save_app(array, DB_file_name):
    save_data_to_json(array, DB_file_name)
    exit()

def load_data_from_json(DB_file_name):
    try:
        with open(DB_file_name, 'r') as file:
            data = json.load(file)
            car_list = [Car(item['color'], item['brand'], item['custumer']) for item in data]
            return car_list
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data

def save_data_to_json(array, DB_file_name):
    with open(DB_file_name, 'w') as file:
        json.dump([item.as_dict() for item in array], file, indent=4)