# user_data.py

def get_user_data():
    first_name = input("What is your first name?: ").strip()
    last_name = input("What is your last name?: ").strip()
    email = input("What is your email address?: ").strip()
    return first_name, last_name, email  # This returns a tuple
