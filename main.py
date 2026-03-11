from colorama import init, Fore
from services import (
    add_client,
    add_lawyer,
    add_case,
    view_all_cases,
    view_client_cases,
    view_lawyer_cases,
    update_case_status,
    show_highest_priority_case,
    view_clients,
    view_lawyers,
    case_statistics
)

init(autoreset=True)


def client_menu():
    while True:
        print(Fore.GREEN + "\n=== Client Menu ===")
        print("1. View My Cases")
        print("2. Back")

        choice = input("Choose an option: ").strip()

        if  choice == "1":
            view_client_cases()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again.")


def lawyer_menu():
    while True:
        print(Fore.YELLOW + "\n=== Lawyer Menu ===")
        print("1. View Assigned Cases")
        print("2. Update Case Status")
        print("3. Show Highest Priority Case")
        print("4. View Lawyers")
        print("5. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_lawyer_cases()
        elif choice == "2":
            update_case_status()
        elif choice == "3":
            show_highest_priority_case()
        elif choice == "4":
            view_lawyers()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


def admin_menu():
    while True:
        print(Fore.CYAN + "\n=== Admin Menu ===")
        print("1. Add Client")
        print("2. Add Lawyer")
        print("3. add Case")
        print("4. View All Cases")
        print("5. View Clients")
        print("6. Case Statistics")
        print("7. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_client()
        elif choice == "2":
            add_lawyer()
        elif choice == "3":
            add_case()   
        elif choice == "4":
            view_all_cases()
        elif choice == "5":
            view_clients()
        elif choice == "6":
            case_statistics()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Try again.")


def main_menu():
    while True:
        print(Fore.MAGENTA + "\n=== LegalFlow ===")
        print("1. Client")
        print("2. Lawyer")
        print("3. Admin")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            client_menu()
        elif choice == "2":
            lawyer_menu()
        elif choice == "3":
            admin_menu()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()