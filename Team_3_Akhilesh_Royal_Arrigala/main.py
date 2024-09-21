from inventory import Inventory
from reorder_system import ReorderSystem
from transfer_system import TransferSystem
from forecasting import Forecasting
from security import Security

def main():

    users = {
        "admin": {"password": "admin123", "role": "admin"},
        "user1": {"password": "userpass", "role": "user"}
    }

    security = Security()
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    authenticated_user = security.authenticate(username, password, users)
    if not authenticated_user:
        print("Authentication failed. Exiting...")
        return

    print("Welcome to the Inventory Management System")
    inventory = Inventory()
    reorder_system = ReorderSystem(inventory)
    transfer_system = TransferSystem(inventory)
    forecasting = Forecasting(inventory)

    while True:
        print("\n--- Main Menu ---")
        print("1. Add New Material")
        print("2. Update Inventory")
        print("3. Display Stock Levels")
        print("4. Check Reorder Requirements")
        print("5. Manage Material Transfer")
        print("6. Generate Reports")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            inventory.add_material()
        elif choice == '2':
            inventory.update_inventory()
        elif choice == '3':
            inventory.display_stock_levels()
        elif choice == '4':
            reorder_system.check_reorder()
        elif choice == '5':
            transfer_system.manage_transfer()
        elif choice == '6':
            forecasting.generate_reports()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    inventory.close()

if __name__ == "__main__":
    main()

