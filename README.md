# Passwordlocker

## Password locker is a simple python app that allows a userto create an account sign in and copy account details on the clipboard.

#### By **[Dickson Kariuki](https://github.com/dicksonkariuki)**

## Description

Password Locker is an application that helps users generate and store passwords on their multiple accounts.
The password locker runs on the terminal and uses short codes to navigate through it.
When starting up the application, the user is met with the following shortcodes:

    1. cc - Creates a new account
    2. ss - Sign in
    3. ex - Exit the application

The user will be met with the following commands while signing in:

    1. ad - Add password
    2. vp - View passwords
    3. cp - Copy password to clipboard
    4. lo - Log out

## Specifications

| Behavior                   | Input                                                      | Output                                                                                       |
| -------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Create new account         | Type: cc <br>Username: dickson <br>Password: kariuki       | User dickson has been created.<br>Log in to Continue                                         |
| Sign in                    | Type: ss <br>Username: dickson<br>Password: kariuki        | Welcome dickson! What would you like to do?                                                  |
| Add Password               | Type: ad <br>Website: gmail.com <br>Length of password: 15 | **Generates a password with x length**<br>Your password for mywebsite.com is wAd8eFh49eds34r |
| View list of passwords     | Type: vp                                                   | Generates a lists of websites and passwords                                                  |
| Copy Password to clipboard | Type: cp <br>Enter index: 1                                | Password 1 on the list has been copied and is ready for pasting                              |
| Log Out                    | Type: lo                                                   | **Logs out the user** <br>Thanks for creating an account with us dickson!                    |
| Exit Application           | Type: ex                                                   | **Closes the application** <br>Thanks for creating an account with us dickson!               |

## System Requirements

    1. You should ensure that your system has Python 3.6 version.

## Set-up and Installation instructions

    - Clone the Repo
    - Install python 3.6
    - Run `python3.6 run.py`

## Known bugs

Currently there are no know errors or bugs in the application.

## Technologies used

    - Python 3.6

## Support and contact details

You can Contact me via dicksonkariuki4@gmail.com for advice on how to improve the application.

### License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, or distribute the software.
