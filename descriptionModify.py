def modifyDescription():
    """
    Modifies the description of any item entered
    :return: None
    """
    filename = 'myStore.txt'
    # open original file to read its contents
    open_file = open(filename,'r')
    # store all contents in the file into a list
    file_content = [i.strip() for i in open_file.readlines()]
    # Create a bool variable to use as a flag
    found = False
    # get item description to search
    search = input('Enter item\'s description: ')
    search = search.strip().lower()
    if search == '':
        print('Invalid Input!')
    else:
        # get the new item description 
        new_description = input('Enter the new item description: ')
        new_description = new_description.strip().lower() 
        if new_description == '':
            print('Invalid Input!')
        else:
            # no two or more items can have the same description
            # check if the new item description entered is already 
            # present in the file, display a message if present or not
            if new_description not in file_content:
                for i in file_content:
                    # if the description entered is in the file
                    # get the index and change the description
                    # to the new description
                    if i == search:
                        # set flag value to True
                        found = True
                        file_content[file_content.index(search)] = new_description
                if found == True:
                    # open the original file to write records back into it
                    open_file = open(filename,'w')
                    for i in file_content:
                        open_file.write(i + '\n')
                    print('\nFile has been modified!')
                else:
                    print(f'\nOoops, an item with description \'{search.title()}\' couldn\'t be found')
            else:
                print(F'\nOoops, an item with description \'{new_description.title()}\' already exist in file')  
        