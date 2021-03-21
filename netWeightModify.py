def modifyNetWeight():
    """
    Modifies the net weight of any item entered
    :return: None
    """
    filename = 'myStore.txt'
    # open original file to read its contents
    open_file = open(filename,'r')
    # Create a bool variable to use as a flag
    found = False
    # store all contents in the file into a list
    file_content = [i.strip() for i in open_file.readlines()]
    try:
        # get item net weight to search
        search = float(input('Enter item\'s net weight: '))
        # get the new item net weight 
        new_net_weight = float(input('Enter the new net weight: '))
    except ValueError:
        print('Invalid input!')
    else:    
        for i in file_content:
            # if the net weight entered is in  the file
            # get the index and change the net weight
            # to the new net weight
            if i == str(search):
                found = True
                file_content[file_content.index(str(search))] = new_net_weight
        if found == True:
            # open the original file to write records back into it
            open_file = open(filename,'w')
            for j in file_content:
                open_file.write(str(j) + '\n')
            print('\nFile has been modified!')
        else:
            print(f'\nOoops, item(s) with net weight \'{search}\' couldn\'t be found')