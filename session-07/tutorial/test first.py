
print («Welcome to the restaurant!»)
menu = {
«Burger»: 4.5,
«Fries»: 2.0,
«Soda»: 1.5,
«Salad»: 3.0,
«Pizza»: 6.0
}
items_ordered = []
i = 0

while True:
    print («What do you want to order?»)
    for item, price in menu. items):
        1 += 1
        print (f»{i}. {item}: ${price:.2f}»)
    user_input = input("Enter the number of the item or done")
    if user_input.isdigit() and 0 < int (user_input) <= len (menu):
        item_name = list (menu. keys)) [int (user_input)-1]
        item_price = menu litem_namel
        items_ordered.append({"name": item_name, "price": item_price})
        print (f"Added {item_name} to your order.")
    if user_input.lower() == "done":
        break
    else:
        print("Invalid")
        