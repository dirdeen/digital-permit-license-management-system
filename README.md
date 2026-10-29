# Digital Permit & Licence Management System

## 1. Project Overview

The Digital Permit & Licence Management System is a Python-based application developed using Object-Oriented Programming (OOP) principles. It provides a simple way to manage permit and licence applications, maintain applicant information, and track the status of applications.

The project demonstrates how Python classes, objects, methods, and a dictionary can be used to organize and manage records in a government service context.

## 2. Project Objectives

- Apply Object-Oriented Programming concepts in Python.
- Create and manage applicant and permit objects.
- Register and display permit and licence applications.
- Update application statuses.
- Use a dictionary to store multiple permit objects.
- Validate user input and prevent duplicate permit IDs.
- Test the system using Python's built-in unit testing framework.

## 3. Technologies Used

- **Programming Language:** Python 3
- **Development Environment:** Visual Studio Code
- **Data Structure:** Python dictionary
- **Testing Framework:** Python `unittest`
- **Version Control:** Git and GitHub

## 4. System Features

- Register permit and licence applications.
- Store applicant details.
- Display existing applications.
- Update application statuses.
- Validate permit types and statuses.
- Prevent duplicate permit IDs.
- Run automated tests to verify system functionality.

### Supported Permit and Licence Types

- Business Permit
- Driving Licence
- Building Permit
- Trading Licence

### Application Statuses

- Submitted
- Under Review
- Approved
- Rejected
- Expired

## 5. Object-Oriented Programming Implementation

The system contains three main classes:

### Applicant

Stores applicant information and provides methods for identifying applicants and creating applicant objects from references.

### Permit

Represents an individual permit or licence application. It stores permit details, applicant information, and the current application status.

### PermitManagementSystem

Manages the permit records. It supports adding applications, displaying records, updating statuses, and validating permit types.

The system uses instance methods, a class method, and a static method to demonstrate different method types in Python.

## 6. Project Structure

```text
Digital_Permit_License_Management_System/
├── main.py
├── test_main.py
├── README.md
├── sample_output.txt
├── test_results.txt
├── screenshots/
└── Digital_Permit_License_Management_Report.docx
```

## 7. Installation and Execution

### Requirements

Install Python 3 on your computer.

### Run the Application

Open the project folder in Visual Studio Code and run:

```bash
python3 main.py
```

### Run the Unit Tests

Execute the following command in the terminal:

```bash
python3 -m unittest -v test_main
```

The test suite checks object creation, dictionary-based storage, status updates, invalid permit types, duplicate permit IDs, and invalid statuses.

## 8. Sample Application Records

The demonstration system includes sample permit applications such as:

- **PER-301:** Business Permit — Under Review
- **PER-302:** Building Permit — Submitted

These records demonstrate how the system stores and displays application information.

## 9. Digital Public Goods Principles

The project considers the following Digital Public Goods principles:

### Open Source

The source code is available for review, learning, and further development through GitHub.

### Inclusion and Accessibility

The application uses a simple text-based interface that can run in a standard Python environment.

### Privacy

The demonstration uses fictional applicant information. Real personal information should not be added to a public repository.

### Modularity and Reusability

The system separates applicant information, permit information, and management operations into distinct classes, making the code easier to understand, maintain, and extend.

## 10. Testing

The project includes automated unit tests in `test_main.py`. These tests are designed to verify the main features and validate how the system handles invalid input.

Actual test results should be confirmed by running the unit test command in the development environment.

## 11. Limitations and Future Improvements

The current version is a basic Python demonstration. Future improvements could include:

- A graphical user interface.
- Database integration for permanent record storage.
- User authentication and role-based access control.
- Application search and filtering.
- Permit renewal and expiry notifications.
- Secure handling of real applicant information.

## 12. Conclusion

The Digital Permit & Licence Management System demonstrates the practical application of Python Object-Oriented Programming in a government service context. It provides basic permit and licence record management while demonstrating classes, objects, methods, data structures, validation, and automated testing.

This project was developed for educational purposes as part of an Object-Oriented Programming assignment.
