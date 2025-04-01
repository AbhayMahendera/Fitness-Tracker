import utils
import auth

def main():
        print("|--------------------------------|")
        print("| Welcome to Fitness Tracker App |")
        print("|--------------------------------|")
        
        choice = input("1. Login\n2. Register\n3. Exit\nChoice: ").strip()

        match choice:
            case "1":
                auth.login()
            case "2":
                auth.signup()
            case "3":
                exit()
            case _:
                print("Invalid choice!")

if __name__ == "__main__":
    main()