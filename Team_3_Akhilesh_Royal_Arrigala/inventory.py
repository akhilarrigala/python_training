from database import Database
class Inventory:
    def __init__(self):
        self.db = Database()

    def update_inventory(self):
        item_id = int(input("Enter Item ID to update: "))
        quantity = int(input("Enter quantity to add: "))
        
        item = self.db.get_item(item_id)
        if item:
            self.db.update_item(item_id, quantity)
            print(f"Updated Item {item_id} by {quantity} units.")
        else:
            print(f"Item {item_id} not found.")

    def add_material(self):
        item_id = int(input("Enter new Item ID: "))
        name = input("Enter new Item name: ")
        stock = int(input("Enter initial stock quantity: "))
        cost_of_goods_sold = float(input("Enter cost of goods sold: "))
        historical_sales = float(input("Enter historical sales: "))
        
        self.db.add_item(item_id, name, stock, cost_of_goods_sold, historical_sales)
        print(f"Added new material: ID {item_id}, Name {name}, Stock {stock}.")

    def display_stock_levels(self):
        items = self.db.get_all_items()
        print("\n--- Current Stock Levels ---")
        for item in items:
            print(f"ID: {item[0]}, Name: {item[1]}, Stock: {item[2]}")

    def close(self):
        self.db.close()
