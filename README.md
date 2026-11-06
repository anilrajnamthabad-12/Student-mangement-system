# Student Management System

A console-based Student Management System written in Python using object-oriented programming (OOP). It lets you add, view, search, update and delete student records from a simple menu, and it saves the data to a JSON file so nothing is lost when the program closes.

## Features

- **Add** a student (ID, name, age, place). Duplicate IDs are not allowed.
- **View** all students.
- **Search** for a student by ID.
- **Update** a student's name, age or place. Press Enter on any field to keep the old value.
- **Delete** a student, with a yes/no confirmation.
- **Save and load**: records are saved to `students.json` after every change and loaded again when the program starts.

## Technologies used

- Python 3
- Object-oriented programming (classes, objects, methods)
- Lists and dictionaries
- JSON file handling (`json` and `os` modules)

## Project structure

```
student-management/
├── student_management.py   # the program
├── students.json           # created automatically when you add the first student
└── README.md
```

### Classes

| Class | Purpose |
|---|---|
| `Student` | Stores one student's details (`id`, `name`, `age`, `place`), shows them, and converts them to a dictionary for saving. |
| `StudentManagement` | Holds the list of students and provides `add_student`, `view`, `search`, `update_student`, `delete_student`, `save` and `load`. |

## How to run

1. Install [Python 3](https://www.python.org/downloads/).
2. Save the code as `student_management.py`.
3. Open a terminal in that folder and run:

```bash
python student_management.py
```

(On some systems use `python3` instead of `python`.)

## Menu

```
1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit
```

Type the number of the option and press Enter.

## Example session

```
1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit
choose: 1
enter id: 1
enter name: asha
enter age: 20
enter place: chennai
student added successfully
```

## How the data is stored

Records are saved in `students.json`, for example:

```json
[
  {
    "id": "1",
    "name": "asha",
    "age": "20",
    "place": "chennai"
  }
]
```

If the file is missing, the program starts with an empty list. If the file is damaged, it prints `could not read the file, starting empty` instead of crashing.

## Known limitations

- Age and ID are stored as text, because `input()` returns text.
- There is no check yet that age is a number or that the name is not empty.
- Search works by exact ID only.

## Possible improvements

- Validate the input (numeric age, non-empty name).
- Search by name, ignoring upper and lower case.
- Sort students by name or age.
- Use a database such as SQLite instead of a JSON file.
- Add unit tests with `pytest`.
- Build a graphical or web interface.

## Author

Your name here
