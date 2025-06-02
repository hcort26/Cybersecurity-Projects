# Password Checker

This project implements a Python-based password strength and compromise checker. It checks if a password meets common strength criteria and if it appears in a known list of compromised passwords.

## 📂 Project Files
- `password_checker.py`: Main script to check password strength and compare against a list of known compromised passwords.
- `xato-net-10-million-passwords-10000.txt`: Sample file containing a list of compromised passwords for reference.

## 🔑 Key Features
- **Password Strength Checking**: Ensures passwords meet common security standards, including:
  - Minimum 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character
- **Compromised Password Check**: Compares the input password against a list of known compromised passwords.
- **Final Recommendation**: Provides clear guidance on whether to use or change the password based on checks.
