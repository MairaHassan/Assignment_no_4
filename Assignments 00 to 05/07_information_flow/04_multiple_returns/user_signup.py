# user_signup.py

from user_data import get_user_data

def main():
    user_info = get_user_data()
    print("\nReceived the following user data:", user_info)

if __name__ == "__main__":
    main()
