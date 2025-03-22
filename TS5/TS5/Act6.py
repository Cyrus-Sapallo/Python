class Item:
    def __init__(self, item_id: int, name: str, description: str, price: float):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("ID must be a positive integer.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class Manager:
    def __init__(self):
        self.items = {}

    def create(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            new_item = Item(item_id, name, description, price)
            self.items[item_id] = new_item
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def read(self):
        if not self.items:
            print("No items found.")
        else:
            for item in self.items.values():
                print(item)

    def update(self, item_id, name=None, description=None, price=None):
        try:
            if item_id not in self.items:
                raise ValueError("Item ID not found.")
            
            item = self.items[item_id]
            
            if name is not None:
                if not name.strip():
                    raise ValueError("Name cannot be empty.")
                item.name = name
            if description is not None:
                item.description = description
            if price is not None:
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                item.price = price
            
            print("Item updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def delete(self, item_id):
        try:
            if item_id not in self.items:
                raise ValueError("Item ID not found.")
            del self.items[item_id]
            print("Item deleted successfully!")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    manager = Manager()
    
    while True:
        print("\nItem Management System:")
        print("1. Create Item")
        print("2. Read Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            try:
                item_id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                description = input("Enter Description: ")
                price = float(input("Enter Price: "))
                manager.create(item_id, name, description, price)
            except ValueError:
                print("Invalid input.")
        elif choice == "2":
            manager.read()
        elif choice == "3":
            try:
                item_id = int(input("Enter ID of item to update: "))
                name = input("Enter new name: ") or None
                description = input("Enter new description: ") or None
                price_input = input("Enter new price: ")
                price = float(price_input) if price_input else None
                manager.update(item_id, name, description, price)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            try:
                item_id = int(input("Enter ID of item to delete: "))
                manager.delete(item_id)
            except ValueError:
                print("Invalid input.")
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")
