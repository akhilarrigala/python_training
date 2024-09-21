from alert_system import AlertSystem

class TransferSystem:
    def __init__(self, inventory):
        self.inventory = inventory
        self.alert_system = AlertSystem()
    
    def manage_transfer(self):
        item_id = int(input("Enter Item ID to transfer: "))
        source = input("Enter source warehouse: ")
        target = input("Enter target warehouse: ")
        quantity = int(input("Enter quantity to transfer: "))
        delay = int(input("Enter transfer delay in hours: "))
        
        if delay > 3:
            print(f"Delay in shipment for Item {item_id}. Delay: {delay} hours.")
            self.alert_system.send_shipment_delay_alert(item_id, delay)
        else:
            self.transfer_item(item_id, source, target, quantity)
    
    def transfer_item(self, item_id, source, target, quantity):
        item = self.inventory.db.get_item(item_id)
        if item and item[2] >= quantity:  # Check if stock is available
            # Deduct stock from source warehouse
            self.inventory.db.update_item(item_id, -quantity)  # Reduce stock for transfer
            print(f"Transferred {quantity} units of Item {item_id} from {source} to {target}.")
            # Optionally, you could add stock to the target warehouse here
            # self.inventory.db.update_item(target_item_id, quantity)  # Uncomment if needed
        else:
            print(f"Insufficient stock for Item {item_id}.")
