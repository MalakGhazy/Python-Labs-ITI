import re # Regex
from utils import load_data,save_data

USERS_FILE = "users.json"

def validate_phone(phone):
    return bool(re.match(r"^01[0-2,5]{1}[0-9]{8}$", phone))

def register():
    users = load_data(USERS_FILE)
    email = input("Enter Email: ").strip()

    for user in users:
        if user["email"] == email:
            print("Email already exists!")
            return  # Stop registration

    password = input("Enter Password: ").strip()
    confirm_password = input("Confirm Password: ").strip()

    if password != confirm_password:
        print("Passwords Do Not Match")
        return
    
    phone = input("Enter Phone Number: ").strip()
    if not validate_phone(phone):
        print("Invalid Phone Number!")
        return
    
    user = {
        "first_name":input("Enter First Name: ").strip(),
        "last_name":input("Enter Last Name: ").strip(),
        "email":email,
        "password":password,
        "phone":phone
    }

    users.append(user)
    save_data(USERS_FILE,users)
    print("Registeration Successful!")

def login():
    users = load_data(USERS_FILE)
    email = input("Enter Email: ").strip()
    password = input("Enter Password: ").strip()

    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login Successful")
            return email
        
    print("Invalid Credentials")
    return None
