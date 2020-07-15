'''Problem  Statement :
Create a library  management system where user can see the book,lend book, donate, return book by using OOPs
Check if the book is there in library or not if not then display user that the book is not available,
'''

#Solution:

#Creating a class Library
class Library:

    #Creating a constructor to get list of books and name
    def __init__(self,list,name):
        self.booksList = list
        self.name = name
        self.lendDict = {}  #Defining a dictionary to lend a book by User

    #Method to displayBooks in the Library
    def displayBooks(self):
        print(f'We have following books in a library : {self.name}')
        for book in self.booksList:
            print(book)

    # Method to lend Books in the Library
    def lendBook(self,user, book):
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                self.booksList.remove(book)
                print('Lender -Book database has been updated.You can take the book now')
            else:
                print(f'Book is already being used by {self.lendDict[book]}')


    #Method to add book to a Library
    def addBook(self,book):
        self.booksList.append(book)
        print('Book has been added to the Library')

    #Method to return book to a Library
    def returnBook(self,book):
        self.lendDict.pop(book)
        self.booksList.append(book)

#Main function
if __name__ == '__main__':
    #Creating an object with a list of book and library name
    nandan = Library(['Python','Rich Dad Poor Dad','Personality Development','Data Science','Machine Learning'],'Samskruti' )

    #Providing user to opt the following
    while(True):
        #Displaying the user_choice
        print(f'Welcome to the {nandan.name} Library, Enter your choice to continue ')
        print('1. Display Books')
        print('2. Lend a book')
        print('3. Add a book')
        print('4. Return a book')

        #Get Choice from User
        user_choice = input()

        # Checking user choice is valid or not, if not valid then goback to initial step
        if user_choice not in ['1','2','3','4']:
            print('User choice is not valid, Retry Again!!')
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            nandan.displayBooks()  #calling displayBook method of class Library

        elif user_choice == 2:
            book = input('Enter the name of the book you want to lend')
            user = input('Enter your name')
            nandan.lendBook(user,book) #calling lendBook method of class Library

        elif user_choice == 3:
            book = input('Enter the name of the book you want to add')
            nandan.addBook(book)   #calling addBook method of class Library

        elif user_choice == 4:
            book = input('Enter the name of the book you want to return')
            nandan.returnBook(book)  #calling returnBook method of class Library

        else:
            print('The input is invalid') #Displaying the invalid input from the user


        #  To continue program until user want to quit
        print('Press q to quit and c to continue')
        user_input = ''  #To clear the error as the user_input was not defined.

        #Checking the condition to quit or to continue
        while(user_input != 'q' and user_input != 'c'):
            user_input  = input()
            if user_input == 'q':
                exit()
            elif user_input == 'c':
                continue
