import hashlib

# Opens the input and output files
with open("accounts.txt", "r") as infile, open("secure_accounts.txt", "w") as outfile:
    for line in infile:
        parts = line.strip().split()
        
        if len(parts) != 2:
            continue  # Skips lines that don't have exactly two columns
        
        username, password = parts
        salt = username[::-1]  # Reverses the username to create salt
        
        # Hashes the password using SHA256 with the salt
        hash_obj = hashlib.sha256((salt + password).encode())
        hashed_password = hash_obj.hexdigest()
        
        # Writes the username and hashed password to the secure file
        outfile.write(f"{username} {hashed_password}\n")

print("Processing complete. Check 'secure_accounts.txt' for output.")