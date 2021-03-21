def get_user_option():
    """
	Returns user option to perform a task
	:return: int
	"""
    print('\n' + ' ' * 4 + 'Options')
    print('-' * 15 + '\n')
    print('1. Add records to the file') 
    print('2. Display records in the file')
    print('3. Search records in the file using the item:')
    print('\ta. Description')
    print('\tb. Net weight')
    print('\tc. Quantity')
    print('4. Modify record in the file using the item:')
    print('\ta. Description')
    print('\tb. Net weight')
    print('\tc. Quantity')
    print('5. Sort and display items in ascending order of their:')
    print('\ta. Description')
    print('\tb. Net weight')
    print('\tc. Quantity')
    print('6. Sort and display items in descending order of their:')
    print('\ta. Description')
    print('\tb. Net weight')
    print('\tc. Quantity')
    print('7. Delete record in the file using item:')
    print('\ta. Description')
    print('\tb. Net weight')
    print('\tc. Quantity')
    print('8.Check the total number of items in the file')
    print('9. End')
    # make a list of valid numbers to be entered by user to perform a task
    available_options = [*range(1,10)]
    try:
        option = int(input('\nEnter a number from the options above to perform a task: '))
    except ValueError:
        print('Invalid Input!')
    else:
        return option if option in available_options else print('Invalid Input!')       
