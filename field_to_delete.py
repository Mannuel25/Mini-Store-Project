from descriptionDelete import deleteUsingDescription
from netWeightDelete import deleteUsingNetWeight
from quantityDelete import deleteUsingQuantity

def get_field_to_delete():
    """
    Gets item\'s field to delete
    :return: None
    """
    print('\n+ Enter a to delete record using item\'s description')
    print('+ Enter b to delete record using item\'s net weight')
    print('+ Enter c to delete record using item\'s quantity')
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
            deleteUsingDescription()
        elif user_input == 'b': 
            deleteUsingNetWeight()
        elif user_input == 'c': 
            deleteUsingQuantity()