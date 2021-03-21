from userOption import get_user_option
from add_records import addRecords
from display_records import displayRecords
from field_to_search import get_field_to_search
from field_to_modify import get_field_to_modify
from sortInAscendingOrder import AscendingOrderSorting
from sortInDescendingOrder import DescendingOrderSorting
from field_to_delete import  get_field_to_delete
from items_in_file import no_of_items_in_file

def main():
    filename = 'myStore.txt'
    open_file = open(filename,'w')
    UserOption = ''
    while UserOption != 9:
        UserOption = get_user_option()
        if UserOption == 1: 
            addRecords()
        elif UserOption == 2: 
            displayRecords()
        elif UserOption == 3: 
            get_field_to_search()
        elif UserOption == 4: 
            get_field_to_modify()
        elif UserOption == 5: 
            AscendingOrderSorting()
        elif UserOption == 6: 
            DescendingOrderSorting()
        elif UserOption == 7: 
            get_field_to_delete()
        elif UserOption == 8: 
            no_of_items_in_file()
                   
main()