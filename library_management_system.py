class Library:
    #Initialization
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}
    
    #Function to Displaying the book
    def displayBooks(self):
        print(f"We have following books in our - '{self.name}' Library --->")
        for book in self.booksList:
            print(book)
    
    #Function to lend the book
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    
    #Function to add the book
    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")
    
    #Function to return the book
    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print("Lender-Book database has been updated.")
            print("Thank You for Returning the book. Hope you like it.")
        else:
            print("Enter the Valid name of Book.")

if __name__ == '__main__':
    lib = Library(['Python', 'Java', 'C Language', 'C++ Basics', 'Algorithms by CLRS', 'Data Structures'], "PlayWithCode")

    while(True):
        print(f"Welcome to the {lib.name} Library. Enter your choice to continue - ")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("Your Choice : ")

        #Input from the user
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            lib.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend : ")
            user = input("Enter your name : ")
            lib.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add : ")
            lib.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return : ")
            lib.returnBook(book)

        else:
            print("Not a valid option")

        # User want to quit or continue
        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue

            else:
                print("Enter your choice Correctly.")