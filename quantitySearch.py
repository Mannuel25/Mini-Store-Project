def searchUsingQuantity():
    """
    Searches records using item\'s quantity
    and displays all details about the item(s)
    :return: None
    """
    filename = 'myStore.txt'
    # open original file to read its contents
    open_file = open(filename,'r')
    # Create a bool variable to use as a flag
    found = False
    try:
        # get item quantity to search
        search = int(input('Enter item\'s quantity: '))
    except ValueError:
        print('Invalid Input!')
    else:
        description = open_file.readline()
        while description != '':
            netWeight = open_file.readline()
            quantity = open_file.readline()
            description = description.strip()
            netWeight = netWeight.strip()
            quantity = quantity.strip()
            if quantity == str(search):
                # set flag value to True
                found  = True
                print('\n' + '-' * 34)
                print('Description:',description.title())
                print('Net Weight:',format(float(netWeight),'.2f') + 'g')
                print(f'Quantity: {quantity}')
                print('-' * 34)
            description = open_file.readline()
        open_file.close()
        # display a message if search value found or not
        if not found: 
            print(F'Ooops, an item with quantity \'{search}\' couldn\'t be found')