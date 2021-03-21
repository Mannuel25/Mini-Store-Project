def modifyItemQuantity():
    """
    Modifies the quantity of any item entered
    :return: None
    """
    filename = 'myStore.txt'
    # open a transient file to write records into
    temporal_file = open('temp_file.txt','w')
    # open original file to read its contents
    open_file = open(filename,'r')
    # Create a bool variable to use as a flag
    found = False
    # store all contents in the file into a list
    file_content = [i.strip() for i in open_file.readlines()]
    try:
        # get item quantity to search
        search = int(input('Enter item\'s quantity: '))
        # get the new item quantity 
        new_quantity = int(input('Enter the new quantity: '))
    except ValueError:
        print('Invalid input!')
    else:    
        for i in file_content:
            # if the quantity entered is in the file
            # get the index and change the quantity
            # to the new quantity 
            if i == str(search):
                found = True
                file_content[file_content.index(str(search))] = new_quantity
        if found == True:
            # open the original file to write records back into it
            open_file = open(filename,'w')
            for j in file_content:
                open_file.write(str(j) + '\n')
            print('\nFile has been modified!')
        else:
            print(f'\nOoops, an item with quantity \'{search}\' couldn\'t be found')