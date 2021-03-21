import os 

def deleteUsingDescription():
    """
    Deletes record of item using its description
    :return: None
    """
    filename = 'myStore.txt'
    # open a transient file to write records into
    temporal_file = open('temp_file.txt','w')
    # open original file to read its contents
    open_file = open(filename,'r')
    # Create a bool variable to use as a flag
    found = False
    # get item description to search
    search = input('Enter item\'s description: ')
    search = search.strip().lower()
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
            # write this record to the transient 
            # file if it\'s not the record to delete
            if search != description:
                temporal_file.write(description + '\n')
                temporal_file.write(str(netWeight).strip() + '\n')
                temporal_file.write(str(quantity).strip() + '\n')
            else: 
                # set flag value to True
                found = True
            description = open_file.readline()    
        open_file.close()
        temporal_file.close()
        # remove the original file
        os.remove('myStore.txt')    
        # rename the transient file
        os.rename('temp_file.txt', 'myStore.txt')  
        # display a message if search value found or not
        if found == True:
            print('File has been modified!') 
        else:
            print(F'Ooops, an item with description \'{search}\' couldn\'t be found')
