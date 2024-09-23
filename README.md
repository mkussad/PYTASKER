# PYTASKER

#### Description:

The PYTASKER project is a Python-based application that provides a simple command-line interface for managing tasks. The application uses an SQLite database to store task information and allows users to perform various operations such as adding tasks, editing existing tasks, marking tasks as completed or incomplete, viewing tasks, deleting tasks, and exporting tasks to a CSV file.

## Files:

### `project.py`

- **Main File**: This file contains the main functionality of the Task Manager. It includes functions for adding, editing, marking as completed or incomplete, viewing, deleting tasks, and exporting tasks to a CSV file. The main menu provides users with options to interact with the task manager.

### `test_project.py`

- **Testing Module**: This file includes unit tests for the functions in `project.py`. Each function in `project.py` has a corresponding test function in this file, ensuring that the code functions as expected and meets the specified requirements.

### `requirements.txt`

- **Dependencies**: This file lists external libraries required for the project. Currently, it includes `colorama` for terminal text coloring. If additional libraries are added in the future, they should be listed here.

## How to Run:

1. Clone the project repository.
2. Navigate to the project folder.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the main program with `python project.py`.

## Design Choices:

- **SQLite Database**: The use of an SQLite database allows for efficient and persistent storage of task data. The `sqlite3` library is employed to interact with the database.

- **Command-Line Interface**: A command-line interface was chosen for simplicity and ease of use. Users can navigate through the options using numerical choices.

- **Colorama for Terminal Coloring**: The `colorama` library enhances the visual experience by providing colored text in the terminal, making it easier for users to distinguish different types of messages.

## Future Enhancements:

- Implementing a graphical user interface (GUI) for a more user-friendly experience.
- Adding user authentication for multi-user functionality.
- Enhancing the testing suite to cover additional edge cases and scenarios.

## Acknowledgments:

This project was developed as part of CS50’s Introduction to Programming with Python. Special thanks to David J. Malan for guidance and support throughout the development process.

Feel free to explore and contribute to the project to make it even more robust and feature-rich!
