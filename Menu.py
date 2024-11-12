# In this menu, we can add items and It will display total prices
# In this project, I am using dictionary and loop.
# Define menu of restro.

menu = {
    'Pizza': 100,
    'Pasta': 150,
    'Burger': 180,
    'Coffee': 200,
    'Salad': 120   
}

print("Welcome To FunFood Restro") # Greet
print("Pizza': 100\nPasta: 150\nBurger: 180\nCoffee: 200\nSalad: 120")

Order_total = 0 # total price of item.

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    Order_total += menu[item_1]
    print(f"your item {item_1} is add to your order, please wait!")
else:
    print(f"we are sorry {item_1} we can not surver you with this item")

another_item = input(" Hey would you like something else? (Yes/No)")  
if another_item == "Yes":
    item_2 = input("Enter the order you like to server") 
    if item_2 in menu:
        Order_total += menu[item_2]
        print(f"your item {item_2} is add to your order, please wait!")
    else:
        print(f"we are sorry {item_2} we can not surver you with this item")

print(f"Your Total Bill is {Order_total}")        





    









