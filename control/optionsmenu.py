def get_menu_choice():
    def print_menu():       # Your menu design here
        print(" _   _ _____ _____      _         _   ")
        print("| \ | |  ___|_   _|    / \   _ __| |_ ")
        print("|  \| | |_    | |     / _ \ | '__| __|")
        print("| |\  |  _|   | |    / ___ \| |  | |_ ")
        print("|_| \_|_|     |_|   /_/   \_\_|   \__|")

        print(30 * "-", "MENU", 30 * "-")
        print("1. Configure contract parameters ")
        print("2. Whitelist wallets ")
        print("3. Get listed wallets ")
        print("4. Start token pre-sale ")        
        print("5. Listen contract events ")                
        print("6. Exit ")
        print(73 * "-")

    loop = True
    int_choice = -1

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-6]: ")

        if choice == '1':
            int_choice = 1
            loop = False
        elif choice == '2':
            choice = ''
            while len(choice) == 0:
                choice = input("Enter custom folder name(s). It may be a list of folder's names (example: c:,d:\docs): ")
            int_choice = 2
            loop = False
        elif choice == '3':
            choice = ''
            while len(choice) == 0:
                choice = input("Enter a single filename of a file with custom folders list: ")
            int_choice = 3
            loop = False
        elif choice == '4':
            choice = ''
            while len(choice) == 0:
                choice = input("Enter a single filename of a conf file: ")
            int_choice = 4
            loop = False
        elif choice == '6':
            int_choice = -1
            print("Exiting..")
            loop = False  # This will make the while loop to end
        else:
            # Any inputs other than values 1-4 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]
