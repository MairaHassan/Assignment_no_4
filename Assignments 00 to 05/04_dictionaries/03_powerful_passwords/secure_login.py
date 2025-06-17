import hashlib

# Provided hash function (you don't need to modify this)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# stored_logins simulates a database of email:hashed_password pairs
stored_logins = {
    "user1@example.com": hash_password("password123"),
    "user2@example.com": hash_password("securepass"),
    "user3@example.com": hash_password("letmein")
}

# Function to validate login
def login(email, password_to_check):
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False

# Example usage
def main():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password):
        print("Login successful!")
    else:
        print("Login failed!")

if __name__ == "__main__":
    main()
