def searchUsingDescription():
    """
    Searches records using item\'s description
    and displays all details about the item
    :return: None
    """
    filename = 'myStore.txt'
    # open original file to read its contents
    open_file = open(filename,'r')
    # get item description to search
    search = input('Enter item\'s description: ')
    search = search.strip().lower()
    # Create a bool variable to use as a flag
    found = False
    while search == '':
        print('Invalid Input!')
        break
    else:
        description = open_file.readline()
        while description != '':
            netWeight = open_file.readline()
            quantity = open_file.readline()
            description = description.strip()
            netWeight = netWeight.strip()
            quantity = quantity.strip()
            if description == search:
                # set flag value to True
                found  = True
                print('\n' + '-' * 34)
                print('Description:',description.title())
                print('Net Weight:',format(float(netWeight),'.2f') + 'g')
                print(f'Quantity: {quantity}')
                print('-' * 34)
            description = open_file.readline()
        open_file.close()
        # display a message if search value not found
        if not found: 
            print(F'Ooops, an item with description \'{search}\' couldn\'t be found')
