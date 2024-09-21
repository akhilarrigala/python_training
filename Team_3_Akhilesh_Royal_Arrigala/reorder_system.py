class ReorderSystem:
    def __init__(self, inventory):
        self.inventory = inventory
    
    def check_reorder(self):
        items = self.inventory.db.get_all_items()
        reorder_needed = False
        print("Checking for reorder requirements...")
        
        for item in items:
            if item[2] < 30:  # Stock level is below threshold
                self.reorder_item(item[0])
                reorder_needed = True
        
        if not reorder_needed:
            print("No items need reordering.")
    
    def reorder_item(self, item_id):
        print(f"Reordering Item {item_id}.")
        print(f"Item {item_id} has been reordered.")
