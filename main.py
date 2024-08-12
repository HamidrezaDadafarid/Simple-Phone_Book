from phonebook import User, PhoneBook


def print_main_menu():
    return (
        "****************************************\n"
        "1- Add new user\n"
        "2- Edit an existing user\n"
        "3- Delete a user based on their name\n"
        "4- Show all users\n"
        "5- Sort the users"
    )


def print_edit_menu():
    return (
        "****************************************\n"
        "1- Edit user's name\n"
        "2- Edit user's phone number\n"
        "3- edit user's email"
    )


def get_user_choice(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return None


def main():
    phone_book = PhoneBook()
    while True:
        print(print_main_menu())
        n = get_user_choice(
            "\nPlease enter the number of your choice (enter 0 to exit): ")

        if n is None:
            continue

        if n == 0:
            print("Exiting the menu. Goodbye!")
            break

        elif n == 1:
            returned_value = phone_book.get_inputs_and_validate_them_for_adding_user()
            if isinstance(returned_value, User):
                if returned_value.name in phone_book.users:
                    print("User already in phonebook!")
                    continue
                print(phone_book.add_user(returned_value))
            elif returned_value is None:
                continue

        elif n == 2:
            print(print_edit_menu())
            edit_choice = get_user_choice(
                "\nPlease enter a number to edit the user's information: ")
            if edit_choice is None:
                continue
            if edit_choice in [1, 2, 3]:
                name = input(
                    "Please enter the name of the user that you want to edit: ")
                if phone_book.validate_name(name) is not True:
                    print(phone_book.validate_name(name))
                    continue
                elif name not in phone_book.users:
                    print("User not found!")
                    continue
                if edit_choice == 1:
                    new_name = input(
                        "Please enter the new name of your user: ")
                    print(phone_book.edit_name(name, new_name))
                elif edit_choice == 2:
                    new_phone_number = input(
                        "Please enter the new phone number of your user: ")
                    print(phone_book.edit_phone_number(
                        name, new_phone_number))
                elif edit_choice == 3:
                    new_email = input(
                        "Please enter the new email of your user: ")
                    print(phone_book.edit_email(name, new_email))
            else:
                print("Please select a valid option between 1 and 3.")
                continue

        elif n == 3:
            name = input(
                "Please enter the user's name you want to delete: ")
            if phone_book.validate_name(name) is not True:
                print(phone_book.validate_name(name))
                continue
            elif name not in phone_book.users:
                print("User not found!")
                continue
            else:
                print(phone_book.delete_user(name))

        elif n == 4:
            phone_book.show_all_users()

        elif n == 5:
            print(phone_book.sort_users())
        else:
            print("Please select a valid option between 1 and 5.")
            continue


if __name__ == "__main__":
    main()
