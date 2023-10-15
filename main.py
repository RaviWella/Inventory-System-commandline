from tabulate import tabulate
import json
import random
import dealer_dictionary
item_dic = {}

def intro():
    from tabulate import tabulate
    x = [
     [ "••••••••••••••••••••••••••••••••••••••••••••••••WELCOME TO ONE NET CAFE - INVENTORY SYSTEM•••••••••••••••••••••••••••••••••••••••••••••••" ],
        ]
    table1 = tabulate(x, tablefmt="rounded_outline")
    print(table1)
    #table = tabulate(data, tablefmt="grid")

def main():
    print( """\033[1m\033[32m
           • Type AID for adding item details.
           • Type DID for deleting item details.
           • Type UID for updating item details.
           • Type VID for viewing the items table.  
           • Type SID for saving the item details to the text file at any time.
           • Type SDD for selecting four dealers randomly from a file.
           • Type VRL for displaying all the details of the randomly selected dealers.  
           • Type LDI for display the items of the given dealer.
           • Type ESC to exit the program.
           \033[0m""")

def load_inventory():
    global item_dic
    try:
        with open("inventory.txt", "r") as file:
            item_dic = json.load(file)
    except FileNotFoundError:
        pass

def save_inventory():
    with open("inventory.txt", "w") as f:
        for item_code, item_details in item_dic.items():
            item_record = f"Item code: {item_code}|Item Name: {item_details['Item Name']}|Item Brand: {item_details['Item Brand']}|Item Price: {item_details['Item Price']}|Item Quantity: {item_details['Item Quantity']}|Item Category: {item_details['Item Category']}|Purchased Date: {item_details['Purchased Date']}\n"
            f.write(item_record)

def add_item():
    print("\033[1m\033[36m•••••••••••••• ADDING ITEM ••••••••••••••\033[0m")
    # create the program to get the input. not an empty spaces.
    item_code = ""
    while not item_code:
        item_code = input("Enter Item Code: ")
        item_code=item_code.strip()
        # check the item code is already in the inventory
        if item_code in item_dic:
            print(f"\033[1m\033[94m{item_code} item already in inventory.\033[0m")
            item_code = ""
            continue

    item_name = ""
    while not item_name:
        item_name = input("Enter Item Name: ")
        item_name=item_name.strip()

    item_brand = ""
    while not item_brand:
        item_brand = input("Enter Item Brand: ")
        item_brand=item_brand.strip()

    item_price = ""
    while not item_price:
        try:
            item_price = float(input("Enter Item Price: "))
            break
        except:
            print(f"\033[1m\033[31mInvalid input. Please enter a valid integer value.\033[0m")
            continue

    item_quantity = ""
    while not item_quantity:
        try:
            item_quantity = int(input("Enter Item Quantity: "))
        except ValueError:
            print(f"\033[1m\033[31mInvalid input. Please enter a valid integer value.\033[0m")
            continue

    item_category = ""
    while not item_category:
        item_category = input("Enter Item Category: ")
        item_category=item_category.strip()

    purchased_date = ""
    while not purchased_date:
        purchased_date = input("Enter Purchased Date (DD/MM/YYYY): ")
        purchased_date=purchased_date.strip()

        item_details = {"Item Name": item_name,
                        "Item Brand": item_brand,
                        "Item Price": item_price,
                        "Item Quantity": item_quantity,
                        "Item Category": item_category,
                        "Purchased Date": purchased_date}

        item_dic[item_code] = item_details
        print(f"\033[1m\033[92m{item_name} ({item_code}) added to inventory.\033[0m")
        # to save the item details to the inventory
        save_inventory()

# deleting items by searching item code:
def delete_item():
    print("\033[1m\033[36m•••••••••••••• DELETING ITEM ••••••••••••••\033[0m")
    item_code = input("Enter Item Code: ")
    if item_code in item_dic:
        del item_dic[item_code]
        print(f"\033[1m\033[93m{item_code} deleted from inventory.\033[0m")
        # to delete the item details from inventory file
        save_inventory()
    else:
         print(f"\033[1m\033[31m{item_code} not found in inventory.\033[0m")

# updating items
def update_item():
    print("\033[1m\033[36m•••••••••••••• UPDATE ITEM ••••••••••••••\033[0m")
    item_code = input("Enter Item Code: ")
    if item_code in item_dic:
        print(f"\033[1m\033[36mEnter new details for the item (Leave blank for no change):\033[0m")
        item_name = input(f"Current Item Name: {item_dic[item_code]['Item Name']}\nNew Item Name: ")
        item_name=item_name.strip()
        item_brand = input(f"Current Item Brand: {item_dic[item_code]['Item Brand']}\nNew Item Brand: ")
        item_brand=item_brand.strip()
        while True:
            try:
                item_price = float(input(f"Current Item Price: {item_dic[item_code]['Item Price']}\nNew Item Price: "))
                break
            except ValueError:
                print(f"\033[1m\033[31mInvalid input. Please enter a valid number value.\033[0m")
        while True:
            try:
                item_quantity = int(input(f"Current Item Quantity: {item_dic[item_code]['Item Quantity']}\nNew Item Quantity: "))
                break
            except ValueError:
                print(f"\033[1m\033[31mInvalid input. Please enter a valid integer value.\033[0m")
        item_category = input(f"Current Item Category: {item_dic[item_code]['Item Category']}\nNew Item Category: ")
        item_category=item_category.strip()
        purchased_date = input(f"Current Purchased Date: {item_dic[item_code]['Purchased Date']}\nNew Purchased Date (DD/MM/YYYY): ")
        purchased_date=purchased_date.strip()

        # save updaated detail to the dictionary
        if item_name:
            item_dic[item_code]['Item Name'] = item_name
        if item_brand:
            item_dic[item_code]['Item Brand'] = item_brand
        if item_price:
            item_dic[item_code]['Item Price'] = float(item_price)
        if item_quantity:
            item_dic[item_code]['Item Quantity'] = int(item_quantity)
        if item_category:
            item_dic[item_code]['Item Category'] = item_category
        if purchased_date:
            item_dic[item_code]['Purchased Date'] = purchased_date

        # to save updated details to inventory file
        save_inventory()
        print(f"\033[1m\033[92m {item_code} ({item_name}) details updated.\033[0m")
        #print(f"{item_code}{item_name} details updated.")
    else:
        print(f"\033[1m\033[31m{item_code} not found in inventory.\033[0m") #red


# viewing added items
def view_items():

    if not item_dic:
        print("\033[1m\033[31mNo items found!\033[0m")
    else:
        print(
            "\033[1m\033[36m•••••••••••••••••••••••••••••••••••••••••••• VIEW ITEM •••••••••••••••••••••••••••••••••••••••••••••••••••••••••\033[0m")

        items = []
        total_purchased_items = 0
        for item_code, item_details in item_dic.items():
            items.append([item_code, item_details["Item Name"], item_details["Item Brand"], item_details["Item Price"],
                          item_details["Item Quantity"], item_details["Item Category"], item_details["Purchased Date"]])
            total_purchased_items += item_details["Item Quantity"]

        # manual sorting of items by item code in descending order
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i][0] < items[j][0]:
                    items[i], items[j] = items[j], items[i]

        headers = ["\033[1mItem ID\033[0m", "\033[1mItem Name\033[0m", "\033[1mItem Brand\033[0m","\033[1mItem Price\033[0m", "\033[1mItem Quantity\033[0m", "\033[1mItem Category\033[0m", "\033[1mPurchased Date\033[0m"]
        print(tabulate(items, headers=headers, tablefmt="heavy_grid"))
        print("\033[1m\033[93mTotal Purchased Items: {}\033[0m".format(total_purchased_items))



while True:

    intro()
    main()

    choice = input("Enter your choice: ")
    choice = choice.upper()
    if choice == 'AID':
        add_item()
        print()

    elif choice == 'DID':
        delete_item()
    elif choice == 'VID':
        view_items()
        print()
    elif choice == 'UID':
        update_item()
        print()


    elif choice == 'SDD':
        dealer_dictionary.ddd()
        try:

            with open('dealers.txt', 'r') as file:
                dealers_json = file.read()
                dealers = json.loads(dealers_json)

            # selecting 4 dealers randomly
            random_dealers = random.sample(list(dealers.keys()), 4)
            print("\033[1m\033[34m4 Dealers are selected Randomly\033[0m")
            print()
        except:
            print("\033[1m\033[31mFile Not Found!\033[0m")
            print()

# Displaying  all  the details  of  the  randomly selected dealer
    elif choice == 'VRL':
        try:

            # Sort using bubble sort method
            for i in range(len(random_dealers)):
                for j in range(len(random_dealers) - i - 1):
                    if dealers[random_dealers[j]]['Location'] > dealers[random_dealers[j + 1]]['Location']:
                        random_dealers[j], random_dealers[j + 1] = random_dealers[j + 1], random_dealers[j]

            rows = []
            for dealer in random_dealers:
                dealer_row = [dealer, dealers[dealer]['Contact_Number'], dealers[dealer]['Location']]
                item_rows_added = False
                for item in dealers[dealer]['items']:
                    if not item_rows_added:
                        rows.append(dealer_row + [item['Item_name'], item['brand'], item['price'], item['quantity']])
                        item_rows_added = True
                    else:
                        rows.append(
                            [None, None, None, item['Item_name'], item['brand'], item['price'], item['quantity']])
                if not item_rows_added:
                    rows.append(dealer_row + [None, None, None, None, None, None, None])

            headers = ['\033[1mDealer Name\033[0m', '\033[1mContact Number\033[0m','\033[1mLocation\033[0m', '\033[1mItem Name\033[0m', '\033[1mBrand\033[0m', '\033[1mprice\033[0m', '\033[1mQuantity\033[0m']

            print(
                "\033[1m\033[36m••••••••••••••••••••••••••••••••••••••• RANDOMLY SELECTED DEALER DETAILS ••••••••••••••••••••••••••••••••••••••••••••••••••••\033[0m")
            print()
            print(tabulate(rows, headers=headers ))
            print()
        except:
            print("\033[1m\033[31mYou have not selected any dealers yet!!!\033[0m")
            print()




# Display the items  of the given dealer
    elif choice == 'LDI':
        try:
            dealer_name = input("Enter Dealer Name ( Please select from the randomly selected dealer table ) :")
            dealer_name=dealer_name.upper()
            dealer_name=dealer_name.strip()

            if dealer_name in random_dealers:
                print(f"\033[1m\033[36mDealer name:  {dealer_name}\033[0m ")


                get_dealer=[]

                for item in dealers[dealer_name]['items']:
                    item_row = [item['Item_name'], item['brand'], item['quantity'],item['price']]
                    get_dealer.append(item_row)
                headers = ['\033[1mItem Name\033[0m', '\033[1mBrand\033[0m', '\033[1mQuantity\033[0m','\033[1mPrice\033[0m']
                print(tabulate(get_dealer, headers=headers, tablefmt='heavy_grid'))

            else:
                #print("Dealer not found!")
                print("\033[1m\033[31mDealer not found! (Please use randomly selected deslers [ VRL ]...) \033[0m")
        except:
            print("\033[1m\033[31mThere are no Randomly Selected Dealers. Please go through the 'SDD' Operation...\033[0m")

    elif choice=='SID':
        save_inventory()
        print(f"\033[1m\033[92mInventory saved to file.\033[0m")

    elif choice == 'ESC':
        print("\033[1m\033[36mGood Bye! Have a nice Day...\033[0m")
        break

    else:
        print("\033[1m\033[31mInvalid choice. Please try again.\033[0m" , choice)

