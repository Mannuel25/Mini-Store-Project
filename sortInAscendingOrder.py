def AscendingOrderSorting():
    """
    Sorts and displays items in ascending order
    of description, net weight, quantity
    :return: None
    """
    filename = 'myStore.txt'
    print('\n+ Enter a to sort in ascending order of item description')
    print('+ Enter b to sort in ascending order of item net weight')
    print('+ Enter c to sort in ascending order of item quantity')
    # make a list of valid letters to be entered by user to perform a task
    possible_picks = ['a','b','c']
    # open original file to read its contents
    open_file = open(filename,'r')
    # make a dictionary consisting of 
    # all details about every item in the file
    items_details = {}
    # make a list to store net weight for each item
    items_net_weight = []
    # make a list to store quantity for each item
    items_quantity = []
    user_input = input('\nEnter a letter to perform a task: ')
    user_input = user_input.strip().lower()
    while user_input not in possible_picks:
        print('Invalid Input!')
        user_input = input('\nEnter a valid letter to perform a task: ')
        user_input = user_input.strip().lower()
    else:
        description = open_file.readline()
        while description != '':
            description = description.strip()
            items_details[description] = []
            netWeight = open_file.readline().strip()
            quantity = open_file.readline().strip()
            items_details[description].append(float(netWeight))
            items_details[description].append(int(quantity))
            description = open_file.readline() 
        # make a list to store all values for each item
        details_values = [*items_details.values()]
        details_values.sort()
        # make a list to store description for each item
        items_descriptions = [i for i in items_details]
        for a in details_values:
            # append each item net weight
            items_net_weight.append(a[0])   
        for b in details_values:
            # append each item quantity
            items_quantity.append(b[1]) 
        items_descriptions.sort()
        items_net_weight.sort()
        items_quantity.sort()
        if user_input == 'a':
            print('\nSorting description in ascending order [a-z]')
            for key,value in sorted(items_details.items()):
                print('\n' + '-' * 34)
                print('Description:',key.title())
                print('Net Weight:',format(float(items_details[key][0]),'.2f') + 'g')
                print(f'Quantity: {items_details[key][1]}')
                print('-' * 34)
        elif user_input == 'b': 
            # make a list to store description of
            # each item in ascending order of their net weight
            new_list = []
            print('\nSorting net weight in ascending order ⬆')
            for t in details_values:
                for i,j in items_details.items():
                    if t == j and i not in new_list:
                        new_list.append(i)
            for a,b in enumerate(details_values):
                for i,j in enumerate(new_list):
                    if a ==i:
                        print('\n' + '-' * 34)
                        print('Net Weight:',format(float(b[0]),'.2f') + 'g')
                        print('Description:',j.title())
                        print(f'Quantity: {b[1]}')
                        print('-' * 34)
        elif user_input == 'c':  
            new_list_1, new_list_2 = [], [] 
            print('\nSorting quantity in ascending order ⬆')
            for j in sorted(details_values):
                j.reverse()
                new_list_1.append(j)
            new_list_1.sort()
            for a in new_list_1:
                a.reverse()
            # append description of each item in 
            # ascending order of their quantity
            for i in new_list_1:
                for a,b in items_details.items():
                    if i == b and a not in new_list_2:
                        new_list_2.append(a)
            for a,b in enumerate(new_list_1):
                for i,j in enumerate(new_list_2):
                    if a ==i:
                        print('\n' + '-' * 34)
                        print(f'Quantity: {b[1]}')
                        print('Description:',j.title())
                        print('Net Weight:',format(float(b[0]),'.2f') + 'g')
                        print('-' * 34)