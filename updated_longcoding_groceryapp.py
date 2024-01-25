class Payment:
    def __init__(self, total_amount):
        self.total_amount = total_amount
        self.paid = False

    def make_payment(self, amount):
        if amount >= self.total_amount:
            self.paid = True
            change = amount - self.total_amount
            print(f"Payment successful. Change: ${change:.2f}")
        else:
            print("Insufficient payment. Please provide enough funds.")

class GroceryItem:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def calculate_total_price(self):
        return self.quantity * self.price_per_unit

class GroceryList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if 1 <= index <= len(self.items):
            del self.items[index - 1]
            print("Item removed from the list.")
        else:
            print("Invalid item index.")

    def update_quantity(self, index, new_quantity):
        if 1 <= index <= len(self.items):
            self.items[index - 1].quantity = new_quantity
            print("Quantity updated.")
        else:
            print("Invalid item index.")

    def calculate_total_amount(self):
        total_amount = sum(item.calculate_total_price() for item in self.items)
        return total_amount

    def display_list(self):
        print("Grocery List:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item.name} - {item.quantity}  - ${item.calculate_total_price():.2f}")

def main():
    grocery_list = GroceryList()

    while True:
        print("\nOptions:")
        print("1. Add item to the list")
        print("2. Remove item from the list")
        print("3. Update quantity of an item")
        print("4. Display the list")
        print("5. Make payment")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the item: ")
            try:
                quantity = int(input("Enter the quantity: "))
                price_per_unit = float(input("Enter the price per unit: $"))
            except ValueError:
                print("Invalid input. Please enter numeric values for quantity and price.")
                continue

            grocery_item = GroceryItem(name, quantity, price_per_unit)
            grocery_list.add_item(grocery_item)
            print("Item added to the list.")

        elif choice == "2":
            grocery_list.display_list()
            index_to_remove = int(input("Enter the index of the item to remove: "))
            grocery_list.remove_item(index_to_remove)

        elif choice == "3":
            grocery_list.display_list()
            index_to_update = int(input("Enter the index of the item to update: "))
            try:
                new_quantity = int(input("Enter the new quantity: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value for the quantity.")
                continue

            grocery_list.update_quantity(index_to_update, new_quantity)

        elif choice == "4":
            grocery_list.display_list()

        elif choice == "5":
            total_amount = grocery_list.calculate_total_amount()
            print(f"Total amount: ${total_amount:.2f}")

            try:
                payment_amount = float(input("Enter the payment amount: $"))
            except ValueError:
                print("Invalid input. Please enter a numeric value for the payment amount.")
                continue

            payment = Payment(total_amount)
            payment.make_payment(payment_amount)

            if payment.paid:
                break  # Exit the loop if payment is successful

        elif choice == "6":
            print("Exiting the grocery application. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()