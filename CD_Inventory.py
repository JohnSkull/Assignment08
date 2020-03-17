#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Create a script that asks the user to select their choice read,
#       write, save, or delete CD inventory data, storing them in a text file.
#       The functionality should be accomplished by the use of classes. 
#       Exceptions should be handled, docstrings updated, read/write functions.
#        
# Change Log:
# Johnh, 2020-Mar-13 Script Created from starter assignment08 .py file
# Johnh, 2020-Mar-13 Assignment and background material consumed in preparation 
#                    for development 
# Johnh, 2020-Mar-14 Added properties cd_id, cd_title, and CD_artist to CD 
#                    class defintion
# Johnh, 2020-Mar-14 Analyzed the organization of the code, imported reusable 
#                    class and function sections from previous assignments 
# Johnh, 2020-Mar-14 Analyzed main body, reused while format, no variables 
#                    handled in the loop, all data handled in classes.
# Johnh, 2020-Mar-14 Initial testing, script runs in Spyder.
# Johnh, 2020-Mar-15 Errors found in 'a', 'l', 's' functions.
# Johnh, 2020-Mar-15 Display method modified to handle the object instantiations
# Johnh, 2020-Mar-16 Testing, error handling, docstrings, readability                   
# Johnh, 2020-Mar-16 Added to Git and submitted
#----------------------------------------#
from os import path

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD: 
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
        
    methods:
        get_id
        get_title
        get_artist
        set_id
        set_title
        set_artist     
    """
    def __init__(self, cd_id, cd_title, cd_artist):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist  
         
    def get_id(self):
        return self.__cd_id
        
    def get_title(self):
        return self.__cd_title
        
    def get_artist(self):
        return self.__cd_artist
        
    def set_id(self, cd_id):
        if not isinstance(cd_id, int):
            raise ValueError("Value is not an Integer")
        self.__cd_id = cd_id
        
    def set_title(self, cd_title):
        if not isinstance(cd_title, str):
            raise ValueError("Value is not a String")
        self.__cd_title = cd_title
        
    def set_artist(self, cd_artist):
        if not isinstance(cd_artist, str):
            raise ValueError("Value is not a String")
        self.__cd_artist = cd_artist 


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
        load_table(lines, table)

    """

    @staticmethod
    def load_inventory(file_name, table, STARTUP = False):
        """Manage data from file to a list of dictionaries in runtime

        Reads the data from file file_name into a list of objects, table 
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of objects): holds the data during runtime

        Returns:
            table
        """ 
        if not STARTUP:
        	print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        	strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        else:
        	strYesNo = "yes"
        
        if strYesNo.lower() == "yes":
        	if path.exists(file_name):
        		print('reloading...')
        		file = open(file_name, "r")
        		lines = []
        		for line in file:
        			line = line.strip()
        			lines.append(line)
        		file.close()
        		if len(lines) > 0:
        			FileIO.load_table(lines, table)
        			IO.show_inventory(table)
        		else:
        			input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        			IO.show_inventory(table)
					
        	else:
        		input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        		IO.show_inventory(table)
        else:
        	input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        	IO.show_inventory(table)
        return table
    
         
    @staticmethod
    def save_inventory(file_name, inventory):
        """Writes the inventory of IDs, CD Names, and Artists to a text file
        
        Args:
            file_name (string): The name of the file that it will write to
            table (list of dict): 2D data structure (list of dicts) holds the data during runtime

        Returns:
            None but saves a file in the directory of the python script
            
        """
        
        IO.show_inventory(inventory)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        
        if strYesNo == 'y':
            # save data
            file = open(file_name, 'w')
            for cd in inventory:
                cd_properties = [str(cd.get_id()), cd.get_title(), cd.get_artist()]
                file.write(','.join(cd_properties) + '\n')
            file.close()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
    
    @staticmethod 
    def load_table(lines, table): 
    	table.clear()
    	for line in lines:
    		cd = line.split(",")
    		cd_id = int(cd[0])
    		cd_title = cd[1]
    		cd_artist = cd[2]
    		table.append(CD(cd_id,cd_title,cd_artist))
    	
    		
# -- PRESENTATION (Input/Output) -- #
class IO:
    """Class definition to handle Input / Output 
       Handling Input / Output
            
    Properties:
        None.

    Methods:
        print_menu(): -> Provides the menu options to the user
        menu_choice(): -> Captures the user's choice
        show_inventory(table): -> Displays current data
    """

    @staticmethod
    def print_menu(): 
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print("Menu\n\n" +
              "[l] load Inventory from file\n" +
              "[a] Add CD\n" + 
              "[i] Display Current Inventory")
              
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of objects): data structure (list of objects) holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in table:
            print('{}\t{} (by:{})'.format(cd.get_id(), cd.get_title(), cd.get_artist()))
        print('======================================')
        
    @staticmethod
    def delete_cd(table):  
        """Deletes a CD row from the table
        
        Args:
            intIDDel (int): ID indicates user entry to delete
            table (list of objects): data structure (list of objects) that holds the data during runtime
            
        Returns:
              table (list of objects): data structure (list of objects) that holds the data during runtime
        """ 
        IO.show_inventory(table)
        # ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # search thru table and delete CD
        blnCDRemoved = False
        for cd in table:            
            if cd.get_id() == intIDDel:
                table.remove(cd)
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        IO.show_inventory(table)
        return table
      
    @staticmethod
    def ask():# Code to get CD data from user
        """Ask user for new ID, CD Title and Artist, values are 
           get and set in CD class
            
           Args:
               None
                
           Returns:
               dicRow (CD object):  An object with cd_id(int), cd_title(str), 
               cd_artist(str) fields to hold the id, title, and artist name respectively.
        """
        
        flag = True
        while flag:
            try:
                objcd_id = int(input('Enter ID: ').strip())
                flag = False
            except ValueError:
                print("INVALID INPUT enter an Integer")
                
        objcd_title = input('What is the CD\'s title? ').strip()            
        objcd_artist = input('What is the Artist\'s name? ').strip()
        dicRow = CD(objcd_id,objcd_title,objcd_artist)
            
        return dicRow    

# -- Main Body of Script -- #
FileIO.load_inventory(strFileName,lstOfCDObjects, True)
IO.print_menu()
strChoice = IO.menu_choice()
while strChoice != 'x':

    if strChoice == 'i':					# show user current inventory
        IO.show_inventory(lstOfCDObjects)
   
    elif strChoice == 'a':					 # let user add data to the inventory
        userCD = IO.ask() 
        lstOfCDObjects.append(userCD)
        IO.show_inventory(lstOfCDObjects)
    
    elif strChoice == 'd':                  # Let user delete data from the Inventory
       lstOfCDObjects = IO.delete_cd(lstOfCDObjects)
    
    elif strChoice == 's':                  # let user save inventory to file
        FileIO.save_inventory(strFileName, lstOfCDObjects)
    
    elif strChoice == 'l':                  # let user load inventory from file
        lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
          
    else:
        print('General Error')#
        
    IO.print_menu()
    strChoice = IO.menu_choice()
    