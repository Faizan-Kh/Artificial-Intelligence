class Restaurant:
    def __init__(self):
        self.menu = {}
        self.ratings = []

    def add_item(self, item, price):
        if item not in self.menu:
            self.menu[item] = price
            print(f"Added '{item}' to the menu with price ${price}.")
        else:
            print(f"'{item}' already exists in the menu.")

    def remove_item(self, item):
        if item in self.menu:
            del self.menu[item]
            print(f"Removed '{item}' from the menu.")
        else:
            print(f"'{item}' is not in the menu.")

    def add_rating(self, rating):
        if 0 <= rating <= 5:
            self.ratings.append(rating)
            print(f"Added rating: {rating}.")
        else:
            print("Rating must be between 0 and 5.")

    def calculate_average_rating(self):
        if self.ratings:
            average_rating = sum(self.ratings) / len(self.ratings)
            print(f"Average rating: {average_rating:.2f}")
        else:
            print("No ratings available.")

# Interactive usage
restaurant = Restaurant()

while True:
    print("\n1. Add Item to Menu")
    print("2. Remove Item from Menu")
    print("3. Add Rating")
    print("4. Calculate Average Rating")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        restaurant.add_item(item, price)
    elif choice == '2':
        item = input("Enter item name to remove: ")
        restaurant.remove_item(item)
    elif choice == '3':
        rating = float(input("Enter rating (0-5): "))
        restaurant.add_rating(rating)
    elif choice == '4':
        restaurant.calculate_average_rating()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
