def displayRecords():
    """
    Reads, displays stored items description with
    their respective net weight and quantities
    :return: None
    """
    filename = 'myStore.txt'
    # open original file to read its contents
    open_file = open(filename,'r')
    description = open_file.readline()
    while description != '':
        netWeight = open_file.readline()
        quantity=open_file.readline()
        description = description.strip().title()
        netWeight = netWeight.strip()
        quantity = quantity.strip()
        print('\n' + '-' * 34)
        print('Description:',description)
        print('Net Weight:',format(float(netWeight),'.2f') + 'g')
        print(f'Quantity: {quantity}')
        print('-' * 34)
        description = open_file.readline()
    open_file.close() 