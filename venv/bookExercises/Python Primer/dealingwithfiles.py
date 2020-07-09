"""File operations and Exceptions"""

try: # lets Try opening the file
    fp = open(r'C:\Users\BEAST\Desktop\plans1.txt', 'r')
    print(fp.read())

except IOError as e: #Just incase it is missing or error in finding it
    print("Ooops! The file was not found \n",e )
    # Error Message, Exception Default Message

