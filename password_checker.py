import re

def is_strong_password(password):
    """Check if the password is strong based on common criteria."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must include at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must include at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must include at least one special character."
    return True, "Password is strong."

def is_compromised_password(password, compromised_file):
    """Check if the password exists in the compromised password list."""
    try:
        with open(compromised_file, 'r', encoding='utf-8', errors='ignore') as file:
            compromised_passwords = set(line.strip() for line in file)
        return password in compromised_passwords
    except FileNotFoundError:
        print(f"Error: The file '{compromised_file}' was not found.")
        return False

def main():
    compromised_file = "xato-net-10-million-passwords-10000.txt"
    password = input("Enter a password to check: ")

    # Step 1: Check password strength
    strong, message = is_strong_password(password)
    print(f"\n[Password Strength Check]: {message}")

    # Step 2: Check against compromised password list
    if is_compromised_password(password, compromised_file):
        print("[Compromised Password Check]: WARNING! This password is found in the compromised list.")
    else:
        print("[Compromised Password Check]: This password is NOT found in the compromised list.")

    # Final Recommendation
    if strong and not is_compromised_password(password, compromised_file):
        print("\nFINAL RESULT: Password is strong and safe.")
    else:
        print("\nFINAL RESULT: Consider changing this password.")

if __name__ == "__main__":
    main()
