from descriptionModify import modifyDescription
from netWeightModify import modifyNetWeight
from quantityModify import modifyItemQuantity

def get_field_to_modify():
    """
    Gets item\'s field to modify
    :return: None
    """
    print('\n+ Enter a to modify item description')
    print('+ Enter b to modify item net weight')
    print('+ Enter c to modify item quantity')
    # make a list of valid letters to be entered by user to perform a task
    possible_picks = ['a','b','c']
    user_input = input('\nEnter a letter to perform a task: ')
    user_input = user_input.strip().lower()
    while user_input not in possible_picks:
        print('Invalid Input!')
        user_input = input('\nEnter a valid letter to perform a task: ')
        user_input = user_input.strip().lower()
    else:
        if user_input == 'a': 
            modifyDescription()
        elif user_input == 'b': 
            modifyNetWeight()
        elif user_input == 'c': 
            modifyItemQuantity()