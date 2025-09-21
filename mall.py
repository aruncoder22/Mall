
menu = {
    "t-shirt": 300,
    "Jeans": 1235,
    "Shirt": 855,
    "Shoes": 1290,
    "vallet": 248,
    "Belt": 200,
    "Jacket": 350,
    "Cap":99
}

def show_menu():
    print("\n===== Shoping Mall=====")
    print(f"{'No.':<5}{'Item':<15}{'Price ':<15}")
    print("-" * 40)

    # menu show
    for i, (item, price) in enumerate(menu.items(), start=1):
        print(f"{i:<5}{item:<15}{price:<15}")
    print("-" * 40)

def calculate_bill(cart):
    total = 0
    print("\n======== Your Bill ===========")
    for item, qty in cart.items():
        price = menu[item] * qty

        total += price 
        print(f"{item:<15} x {qty : <5} = \u20B9 {price:<8}")
    print("-" * 40)

    print(f"Total Amount :\u20B9 {total}")
    print("======Thank You for Shopping======")
    print("Visit Again")

    

def mall():
    
      cart = {}
      while True:
        show_menu()
        choice = input("Do you want to buy an item? (yes/no): ")

        if choice.lower() in ["no", "n",'NO','No']:
            break
        try:    
          item_no = int(input("Select the item number (1-8): "))
        except:
          print("Enter Valid Number Please !")
          item_no = int(input("select the item no (1-8) .."))  
        if 1 <= item_no <= len(menu):
            try:
               qty = int(input("How many do you want quantity  ..  "))
            except:
              print("Invalid input quantity ")
              qty = int(input("How many do you want quantity  .. "))
              

            # item name nikalna
            item_name = list(menu.keys())[item_no - 1]
            cart[item_name] = cart.get(item_name, 0) + qty

            print(f"{qty} {item_name}s added to cart .")
            
          
        else:
            print("Invalid item number! Please choose again.")
      if cart:
       calculate_bill(cart)
      else:
         print("Your cart is empty. Nothing to calculate.")
    

# main program
mall()
