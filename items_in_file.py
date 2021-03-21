def no_of_items_in_file():
   """
   Displays the total number of
   items in the file
   :return: None
   """
   filename = 'myStore.txt'
   # open original file to read its contents
   open_file = open(filename,'r')
   description = open_file.readline() 
   # make a variable to count the number of items
   TOTAL = 0
   while description != '':
      TOTAL += 1
      description = open_file.readline()
   open_file.close()
   # since each record consists of three fields
   # divide the total number of items by 3
   # in the file and round it to the nearest whole number
   print(f'Total number of items in file: {round(TOTAL / 3)}')