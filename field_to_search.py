from descriptionSearch import searchUsingDescription
from netWeightSeacrh import searchUsingNetWeight
from quantitySearch import searchUsingQuantity

def get_field_to_search():
    """
    Gets item\'s field to search
    :return: None
    """
    filename = 'myStore.txt'
    print('\n+ Enter a to search using item\'s description')
    print('+ Enter b to search using item\'s net weight')
    print('+ Enter c to search using item\'s quantity')
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
            searchUsingDescription()
        elif user_input == 'b': 
            searchUsingNetWeight()
        elif user_input == 'c': 
            searchUsingQuantity()