from phonebook import User, PhoneBook


def print_main_menu():
    return "****************************************\n1- Add new user\n2- Edit an existing user\n3- Delete a user based on their name\n4- Show all users\n5- Sort the users"


def print_edit_menu():
    return "****************************************\n1- Edit user's name\n2- Edit user's phone number\n3- edit user's email"


def main():
    phone_book = PhoneBook()
    while True:
        print(print_main_menu())
        try:
            n = int(
                input("\nPlease enter the number of your choice (enter 0 to exit): "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Exiting the menu. Goodbye!")
            break
        else:
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
                elif not returned_value:
                    continue
                else:
                    print("\nKeyboard interrupt detected. Exiting the menu. Goodbye!")
                    break
            elif n == 2:
                print(print_edit_menu())
                try:
                    n = int(
                        input(
                            "\nPlease enter a number to edit the user's information: ")
                    )
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                except KeyboardInterrupt:
                    print("\nKeyboard interrupt detected. Exiting the menu. Goodbye!")
                    break
                else:
                    try:
                        if n in [1, 2, 3]:
                            name = input(
                                "Please enter the name of the user that you want to edit: ")
                            if phone_book.validate_name(name) != True:
                                print(phone_book.validate_name(name))
                                continue
                            elif name not in phone_book.users:
                                print("User not found!")
                                continue
                            if n == 1:
                                new_name = input(
                                    "Please enter the new name of your user: ")
                                print(phone_book.edit_name(name, new_name))
                            elif n == 2:
                                new_phone_number = input(
                                    "Please enter the new phone number of your user: ")
                                print(phone_book.edit_phone_number(
                                    name, new_phone_number))
                            elif n == 3:
                                new_email = input(
                                    "Please enter the new email of your user: ")
                                print(phone_book.edit_email(name, new_email))
                        else:
                            print("Please select a valid option between 1 and 3.")
                            continue
                    except KeyboardInterrupt:
                        print(
                            "\nKeyboard interrupt detected. Exiting the menu. Goodbye!")
                        break

            elif n == 3:
                name = input(
                    "Please enter the user's name you want to delete: ")
                if phone_book.validate_name(name) != True:
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
