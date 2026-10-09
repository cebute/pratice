resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []



def find_resource(resource_id):

    for resource in resources:
        if resource["id"].upper() == resource_id.upper():
            return resource
    return None


def add_resource():

    resource_id = input("Enter resource ID: ").strip().upper()

    if find_resource(resource_id):
        print("Error: A resource with that ID already exists.")
        return

    name = input("Enter resource name: ").strip()
    if not name:
        print("Error: Resource name cannot be empty.")
        return

    category = input("Enter category: ").strip()
    if not category:
        print("Error: Category cannot be empty.")
        return

    try:
        total = int(input("Enter total units: "))

        if total <= 0:
            print("Error: Total units must be greater than 0.")
            return

    except ValueError:
        print("Error: Total units must be a valid integer.")
        return

    resources.append({
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    })

    print(f"Resource '{name}' added successfully.")

def list_resources():
    print("\n--- Resource Inventory ---")

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        print(
            f"ID: {resource['id']} | "
            f"Name: {resource['name']} | "
            f"Category: {resource['category']} | "
            f"Total: {resource['total']} | "
            f"Available: {resource['available']} | "
            f"Borrowed: {borrowed}"
        )

def borrow_resource():
    """Allow a fellow to borrow a resource."""
    fellow_id = input("Enter fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("Error: Fellow ID does not exist.")
        return

    resource_id = input("Enter resource ID: ").strip().upper()
    resource = find_resource(resource_id)

    if resource is None:
        print("Error: Resource ID does not exist.")
        return

    try:
        quantity = int(input("Enter quantity to borrow: "))

        if quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            return

    except ValueError:
        print("Error: Quantity must be a valid integer.")
        return

    if quantity > resource["available"]:
        print(
            f"Error: Only {resource['available']} "
            f"unit(s) of {resource['name']} are available."
        )
        return

    # Only mutate state after every validation has passed.
    resource["available"] -= quantity

    borrow_records.append({
        "fellow_id": fellow_id,
        "resource_id": resource["id"],
        "quantity": quantity
    })

    print(
        f"Success: {fellows[fellow_id]} borrowed "
        f"{quantity} {resource['name']}(s)."
    )
    print(f"Available {resource['name']} units: {resource['available']}")

def return_resource():
    fellow_id = input("Enter fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("Error: Fellow ID does not exist.")
        return

    resource_id = input("Enter resource ID: ").strip().upper()
    resource = find_resource(resource_id)

    if resource is None:
        print("Error: Resource ID does not exist.")
        return

    try:
        quantity = int(input("Enter quantity to return: "))

        if quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            return

    except ValueError:
        print("Error: Quantity must be a valid integer.")
        return

    currently_borrowed = 0

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource["id"]
        ):
            currently_borrowed += record["quantity"]

    if quantity > currently_borrowed:
        print(
            f"Error: {fellows[fellow_id]} currently has only "
            f"{currently_borrowed} unit(s) of {resource['name']} on loan."
        )
        return

    remaining = quantity

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource["id"]
            and remaining > 0
        ):
            amount_to_return = min(record["quantity"], remaining)

            record["quantity"] -= amount_to_return
            remaining -= amount_to_return

    borrow_records[:] = [
        record for record in borrow_records
        if record["quantity"] > 0
    ]

    resource["available"] += quantity

    print(
        f"Success: {fellows[fellow_id]} returned "
        f"{quantity} {resource['name']}(s)."
    )
    print(f"Available {resource['name']} units: {resource['available']}")

def search_resources():
    search_term = input("Enter resource name to search: ").strip().lower()

    if not search_term:
        print("Error: Search term cannot be empty.")
        return

    matches = []

    for resource in resources:
        if search_term in resource["name"].lower():
            matches.append(resource)

    if not matches:
        print("No resources found.")
        return

    print("\n--- Search Results ---")

    for resource in matches:
        print(
            f"ID: {resource['id']} | "
            f"Name: {resource['name']} | "
            f"Category: {resource['category']} | "
            f"Available: {resource['available']}"
        )
        
def filter_by_category():
    category = input("Enter category: ").strip().lower()

    if not category:
        print("Error: Category cannot be empty.")
        return

    matches = []

    for resource in resources:
        if resource["category"].lower() == category:
            matches.append(resource)

    if not matches:
        print("No resources found in that category.")
        return

    print("\n--- Category Results ---")

    for resource in matches:
        print(
            f"ID: {resource['id']} | "
            f"Name: {resource['name']} | "
            f"Category: {resource['category']} | "
            f"Available: {resource['available']}"
        )


def filter_by_category():
    """Display resources belonging to a category."""
    category = input("Enter category: ").strip().lower()

    if not category:
        print("Error: Category cannot be empty.")
        return

    matches = []

    for resource in resources:
        if resource["category"].lower() == category:
            matches.append(resource)

    if not matches:
        print("No resources found in that category.")
        return

    print("\n--- Category Results ---")

    for resource in matches:
        print(
            f"ID: {resource['id']} | "
            f"Name: {resource['name']} | "
            f"Category: {resource['category']} | "
            f"Available: {resource['available']}"
        )


def generate_report():
    """Generate the required inventory and borrowing report."""
    total_units = sum(resource["total"] for resource in resources)
    available_units = sum(resource["available"] for resource in resources)
    borrowed_units = total_units - available_units

    low_stock = [
        resource
        for resource in resources
        if resource["available"] < 3
    ]

    borrowed_amounts = {
        resource["id"]: resource["total"] - resource["available"]
        for resource in resources
    }

    highest_borrowed = max(borrowed_amounts.values())

    most_borrowed = [
        resource
        for resource in resources
        if borrowed_amounts[resource["id"]] == highest_borrowed
    ]

    print("\n========== REPORT ==========")
    print(f"Total units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Units currently borrowed: {borrowed_units}")

    print("\nResources with fewer than 3 available units:")

    if low_stock:
        for resource in low_stock:
            print(
                f"- {resource['name']} "
                f"({resource['available']} available)"
            )
    else:
        print("- None")

    print("\nResource(s) with most units currently borrowed:")

    for resource in most_borrowed:
        borrowed = borrowed_amounts[resource["id"]]

        print(
            f"- {resource['name']} "
            f"({borrowed} borrowed)"
        )

    print("============================")


def display_menu():
    """Display the main menu."""
    print("\n====== CAMPUS RESOURCE MANAGEMENT SYSTEM ======")
    print("1. Add resource")
    print("2. List resources")
    print("3. Borrow resource")
    print("4. Return resource")
    print("5. Search resources")
    print("6. Filter by category")
    print("7. Generate report")
    print("8. Exit")
    print("==============================================")


def main():
    """Run the application menu."""
    while True:
        display_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_resource()

        elif choice == "2":
            list_resources()

        elif choice == "3":
            borrow_resource()

        elif choice == "4":
            return_resource()

        elif choice == "5":
            search_resources()

        elif choice == "6":
            filter_by_category()

        elif choice == "7":
            generate_report()

        elif choice == "8":
            print("Thank you for using the Campus Resource Management System.")
            break

        else:
            print("Error: Invalid menu choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()