# Phonebook Management System

## Overview

This is a command-line-based Phonebook Management System implemented in Python. It allows users to add, edit, delete, display, and sort contacts. The application also supports persistent storage by saving contact information to a JSON file, ensuring data is not lost between sessions.

## Features

- **Add New User**: Add a new contact with a name, phone number, and email.
- **Edit Existing User**: Modify an existing contact's name, phone number, or email.
- **Delete User**: Remove a contact from the phonebook by their name.
- **Show All Users**: Display all contacts in the phonebook.
- **Sort Users**: Sort contacts alphabetically by name.
- **Persistent Storage**: All contacts are saved to `phonebook.json` and automatically loaded when the program starts.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the project files.
2. Ensure you have Python 3 installed on your machine.

## Usage

1. Navigate to the project directory.
2. Run the program using the following command:

    ```bash
    python main.py
    ```

3. Follow the on-screen instructions to interact with the phonebook.

### Main Menu Options

- **1 - Add New User**: Prompts for name, phone number, and email. Validates the inputs and adds the contact.
- **2 - Edit Existing User**: Allows editing of an existing user's name, phone number, or email.
- **3 - Delete User**: Deletes a user from the phonebook by name.
- **4 - Show All Users**: Displays all stored contacts with their details.
- **5 - Sort Users**: Sorts the contacts alphabetically by name.
- **0 - Exit**: Exits the program.

### Editing a User

When editing a user, you will first need to select what you want to edit:
- **1 - Edit User's Name**: Change the contact's name.
- **2 - Edit User's Phone Number**: Update the phone number.
- **3 - Edit User's Email**: Update the email address.

### Persistent Storage

- The program saves all contacts in `phonebook.json` after any operation that modifies the data (add, edit, delete, sort).
- The contacts are automatically loaded from `phonebook.json` when the program starts.

### Error Handling

- The program validates all inputs (name, phone number, email) to ensure they conform to expected formats.
- Appropriate error messages are displayed for invalid inputs or operations.

## File Structure

- **main.py**: The main entry point of the program containing the user interface and menu logic.
- **phonebook.py**: Contains the `PhoneBook` and `User` classes, including all business logic for managing contacts.

## License

This project is open-source and available under the MIT License.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## Contact

If you have any questions or feedback, please contact Hamidreza Dadafarid at hamidreza.dadafarid@aut.ac.ir.

