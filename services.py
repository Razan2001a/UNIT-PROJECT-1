from tabulate import tabulate
from storage import load_data, save_data, CLIENT_FILE, LAWYER_FILE, CASE_FILE
from priority import highest_priority


def add_client():
    clients = load_data(CLIENT_FILE)

    client_id = input("Enter client ID: ").strip()
    name = input("Enter client name: ").strip()

    if not client_id or not name:
        print("Client ID and name are required.")
        return

    for client in clients:
        if client["id"] == client_id:
            print("Client ID already exists.")
            return

    client = {
        "id": client_id,
        "name": name
    }

    clients.append(client)
    save_data(CLIENT_FILE, clients)
    print("Client added successfully.")


def add_lawyer():
    lawyers = load_data(LAWYER_FILE)

    lawyer_id = input("Enter lawyer ID: ").strip()
    name = input("Enter lawyer name: ").strip()

    if not lawyer_id or not name:
        print("Lawyer ID and name are required.")
        return

    for lawyer in lawyers:
        if lawyer["id"] == lawyer_id:
            print("Lawyer ID already exists.")
            return

    lawyer = {
        "id": lawyer_id,
        "name": name
    }

    lawyers.append(lawyer)
    save_data(LAWYER_FILE, lawyers)
    print("Lawyer added successfully.")


def add_case():
    cases = load_data(CASE_FILE)
    clients = load_data(CLIENT_FILE)
    lawyers = load_data(LAWYER_FILE)

    case_id = input("Enter case ID: ").strip()
    title = input("Enter case title: ").strip()
    client_id = input("Enter client ID: ").strip()
    lawyer_id = input("Enter lawyer ID: ").strip()
    case_type = input("Enter case type (criminal/labor/financial/family): ").strip().lower()

    if not case_id or not title or not client_id or not lawyer_id:
        print("All fields are required.")
        return

    for case in cases:
        if case["id"] == case_id:
            print("Case ID already exists.")
            return

    client_exists = any(client["id"] == client_id for client in clients)
    if not client_exists:
        print("Client ID does not exist.")
        return

    lawyer_exists = any(lawyer["id"] == lawyer_id for lawyer in lawyers)
    if not lawyer_exists:
        print("Lawyer ID does not exist.")
        return

    try:
        importance = int(input("Enter importance (1-5): ").strip())
        if importance < 1 or importance > 5:
            print("Importance must be between 1 and 5.")
            return
    except ValueError:
        print("Importance must be a number.")
        return

    try:
        hearing_days = int(input("Enter days until hearing: ").strip())
        if hearing_days < 0:
            print("Days until hearing cannot be negative.")
            return
    except ValueError:
        print("Days until hearing must be a number.")
        return

    case = {
        "id": case_id,
        "title": title,
        "client_id": client_id,
        "lawyer_id": lawyer_id,
        "type": case_type,
        "importance": importance,
        "hearing_days": hearing_days,
        "status": "open"
    }

    cases.append(case)
    save_data(CASE_FILE, cases)
    print("Case added successfully.")


def view_all_cases():
    cases = load_data(CASE_FILE)

    if not cases:
        print("No cases found.")
        return

    table = []
    for case in cases:
        table.append([
            case["id"],
            case["title"],
            case["client_id"],
            case["lawyer_id"],
            case["type"],
            case["status"],
            case["importance"],
            case["hearing_days"]
        ])

    print(tabulate(
        table,
        headers=["ID", "Title", "Client", "Lawyer", "Type", "Status", "Importance", "Hearing Days"],
        tablefmt="grid"
    ))


def view_client_cases():
    cases = load_data(CASE_FILE)
    client_id = input("Enter your client ID: ").strip()

    filtered_cases = [case for case in cases if case["client_id"] == client_id]

    if not filtered_cases:
        print("No cases found for this client.")
        return

    table = []
    for case in filtered_cases:
        table.append([
            case["id"],
            case["title"],
            case["type"],
            case["status"],
            case["importance"],
            case["hearing_days"]
        ])

    print(tabulate(
        table,
        headers=["ID", "Title", "Type", "Status", "Importance", "Hearing Days"],
        tablefmt="grid"
    ))

def view_lawyer_cases():
    cases = load_data(CASE_FILE)
    lawyer_id = input("Enter your lawyer ID: ").strip()

    filtered_cases = [case for case in cases if case["lawyer_id"] == lawyer_id]

    if not filtered_cases:
        print("No cases found for this lawyer.")
        return

    table = []
    warnings = []

    for case in filtered_cases:

        if case["hearing_days"] <= 3:
            warnings.append(
                f"⚠ Case {case['id']} hearing in {case['hearing_days']} days"
            )

        table.append([
            case["id"],
            case["title"],
            case["client_id"],
            case["type"],
            case["status"],
            case["importance"],
            case["hearing_days"]
        ])

    print(tabulate(
        table,
        headers=["ID", "Title", "Client", "Type", "Status", "Importance", "Hearing Days"],
        tablefmt="grid"
    ))

    if warnings:
        print("\nUpcoming Hearings:")
        for w in warnings:
            print(w)

def update_case_status():
    cases = load_data(CASE_FILE)
    case_id = input("Enter case ID to update: ").strip()

    for case in cases:
        if case["id"] == case_id:
            new_status = input("Enter new status (open/in progress/closed): ").strip().lower()

            if new_status not in ["open", "in progress", "closed"]:
                print("Invalid status.")
                return

            case["status"] = new_status
            save_data(CASE_FILE, cases)
            print("Case status updated successfully.")
            return

    print("Case not found.")


def show_highest_priority_case():
    cases = load_data(CASE_FILE)
    best_case, best_score, reasons = highest_priority(cases)

    if best_case is None:
        print("No cases available.")
        return

    print("\nHighest Priority Case")
    print(f"Case ID: {best_case['id']}")
    print(f"Title: {best_case['title']}")
    print(f"Type: {best_case['type']}")
    print(f"Status: {best_case['status']}")
    print(f"Importance: {best_case['importance']}")
    print(f"Hearing in: {best_case['hearing_days']} days")
    print(f"Priority Score: {best_score}")
    print("Reason:")
    for reason in reasons:
        print(f"- {reason}")


def view_clients():
    clients = load_data(CLIENT_FILE)

    if not clients:
        print("No clients found.")
        return

    table = []
    for client in clients:
        table.append([client["id"], client["name"]])

    print(tabulate(table, headers=["Client ID", "Client Name"], tablefmt="grid"))


def view_lawyers():
    lawyers = load_data(LAWYER_FILE)

    if not lawyers:
        print("No lawyers found.")
        return

    table = []
    for lawyer in lawyers:
        table.append([lawyer["id"], lawyer["name"]])

    print(tabulate(table, headers=["Lawyer ID", "Lawyer Name"], tablefmt="grid"))
def case_statistics():
    cases = load_data(CASE_FILE)

    if not cases:
          print("No cases found.")
          return

    total_cases = len(cases)
    open_cases = 0
    in_progress_cases = 0
    closed_cases = 0
    high_importance_cases = 0
    upcoming_hearings = 0

    for case in cases:
        if case["status"] == "open":
            open_cases += 1
        elif case["status"] == "in progress":
            in_progress_cases += 1
        elif case["status"] == "closed":
               closed_cases += 1

    if case["importance"] >= 4:
             high_importance_cases += 1
 
    if case["hearing_days"] <= 3 and case["status"] != "closed":
             upcoming_hearings += 1

    print("\n=== Case Statistics ===")
    print(f"Total Cases: {total_cases}")
    print(f"Open Cases: {open_cases}")
    print(f"In Progress Cases: {in_progress_cases}")
    print(f"Closed Cases: {closed_cases}")
    print(f"High Importance Cases: {high_importance_cases}")
    print(f"Upcoming Hearings (<=3 days): {upcoming_hearings}") 