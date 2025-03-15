from auth import register, login
from projects import project_menu

def main():
    while True:
        print("\nCrowdfunding Console App")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            user_email = login()
            if user_email:
                project_menu(user_email)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()