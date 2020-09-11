def menu():
    print("    1 - Add a Contact")
    print("    2 - Search a Contact")
    print("    3 - Delete a Contact")
    print("    4 - List Contacts")
    print("    5 - Exit")

def write_contacts():
    f = open("book.txt", "a")
    for name in book.keys():
        f.write(name + ":" + book[name] + "\n")
    f.close()

def load_contacts():
    f = open("book.txt", "r")
    for line in f:
        line = line.split(':')
        name = line[0]
        phone = line[1]
        book[name] = phone
    f.close()

def add_contact():
    name = input('Name: ')
    phone = input('Telephone Number: ')
    book[name] = phone
    write_contacts()

def search_contact():
    load_contacts()
    name = input('Name: ')
    print("Their number is:", book[name])

def delete_contact():
    load_contacts()
    name = input('Name: ')
    del book[name]
    write_contacts()

def list_contacts():
    load_contacts()
    for x in book:
        print(x)
while 1:
    print("Welcome to the Sufuk's Phone Book!")
    book = {}
    menu()
    choice = input("Enter an option: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        list_contacts()
    elif choice == '5':
        break
    else:
        print("Invalid input try again")
