def addRecords():
    """
    Writes items and their respective 
    net weight(in grams) and quantities to a file
    :return: None
    """
    filename = 'myStore.txt'
    add_record = input('\nWanna add records? (yes/no): ')
    add_record = add_record.strip().upper()
    while add_record == 'Y' or add_record == 'YES':
        try:
            description = input('\nEnter item\'s description: ')
            description = description.strip().lower()
            while description == '':
                print('Invalid Input!')
                description = input('\nEnter a valid item description: ')
                description = description.strip().lower()
            else:
                netWeight = float(input('Enter item\'s net weight(in grams): '))  
                quantity = int(input('Enter item\'s available quantity: '))  
        except ValueError:
            print('Invalid Input!')
        else: 
            # open the file in read mode to read its contents
            open_file = open(filename,'r')  
            # store all contents in the file into a list
            file_content = [i.strip() for i in open_file.readlines()]
            # if item already present in original file,
            # display a message else write the item and its
            # details to the file
            if description in file_content:
                print(f'\nOoops, an item with description \'{description.title()}\' already exist in file')
                break
            else:
                # open the file in append mode to add records into it
                open_file = open(filename,'a')
                open_file.write(description.strip().lower() + '\n')
                open_file.write(str(netWeight) + '\n')
                open_file.write(str(quantity) + '\n')
                print('\nRecord added successfully!')
                add_record= input('\nWanna add more records? (yes/no): ')
                add_record = add_record.strip().upper()
            open_file.close()
