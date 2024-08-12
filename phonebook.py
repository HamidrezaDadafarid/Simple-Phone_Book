import re
import os
import json
from typing import Union, Optional


class User:
    def __init__(self, name: str, phone_number: str, email: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email


class PhoneBook:
    def __init__(self, filename="phonebook.json"):
        self.filename = filename
        self.users = {}
        self.load_users_from_file()

    def validate_name(self, name: str) -> Union[str, bool]:
        if not name:
            return "User's name should not be empty!"
        if len(name) < 1 or len(name) > 50:
            return "User's name length must be from 1 to 50 characters!"
        pattern = re.compile(r"^[A-Za-z0-9\s'-]+$")
        if not pattern.match(name):
            return "User's name has some invalid characters. it should only contain a-z, A-Z, whitespaces and - characters!"

        return True

    def validate_phone_number(self, phone_number: str) -> Union[str, bool]:
        if not phone_number:
            return "User's phone number should not be empty!"
        if not phone_number.isdigit():
            return "User's phone number must only be digits!"
        pattern = re.compile(r"^09\d{9}$")
        if not pattern.match(phone_number):
            return "User's phone number must be 11 digits. (09...)"

        return True

    def validate_email(self, email: str) -> Union[str, bool]:
        if not email:
            return "User's email should not be empty!"
        pattern = re.compile(
            r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        if not pattern.match(email):
            return "User's email is invalid!"

        return True

    def get_inputs_and_validate_them_for_adding_user(self) -> Union[User, KeyboardInterrupt, None]:
        try:
            name = input("Please enter your user's name: ")
            if self.validate_name(name) != True:
                print(self.validate_name(name))
                return None
            phone_number = input("Please enter your user's phone number: ")
            if self.validate_phone_number(phone_number) != True:
                print(self.validate_phone_number(phone_number))
                return None
            email = input("Please enter your user's email: ")
            if self.validate_email(email) != True:
                print(self.validate_email(email))
                return None

            return User(name, phone_number, email)

        except KeyboardInterrupt:
            return KeyboardInterrupt

    def add_user(self, user: User) -> str:
        self.users[user.name] = {
            "phone_number": user.phone_number,
            "email": user.email,
        }
        self.save_users_to_file()
        return "User added successfully!"

    def edit_name(self, name: str, new_name: str) -> str:
        if self.validate_name(new_name) == True:
            self.users[new_name] = self.users.pop(name)
            self.save_users_to_file()
            return "User's name edited successfully!"
        return self.validate_name(new_name)

    def edit_phone_number(self, name: str, new_phone_number: str) -> str:
        if self.validate_phone_number(new_phone_number) == True:
            self.users[name]["phone_number"] = new_phone_number
            self.save_users_to_file()
            return "User's phone number edited successfully!"
        return self.validate_phone_number(new_phone_number)

    def edit_email(self, name: str, new_email: str) -> str:
        if self.validate_email(new_email) == True:
            self.users[name]["email"] = new_email
            self.save_users_to_file()
            return "User's email edited successfully!"
        return self.validate_email(new_email)

    def delete_user(self, name: str) -> str:
        if name in self.users:
            del self.users[name]
            self.save_users_to_file()
            return "User deleted successfully!"
        return "User is not in the phone book!"

    def show_all_users(self):
        for name, information in self.users.items():
            print(f"Name: {name}\nPhoneNumber: {
                  information["phone_number"]}\nEmail: {information["email"]}\n")

    def sort_users(self) -> str:
        self.users = dict(sorted(self.users.items()))
        self.save_users_to_file()
        return "Users sorted successfully!"

    def save_users_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.users, file, indent=4)

    def load_users_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.users = json.load(file)
