Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
lost_items = []
... found_items = []
... 
... # Report Lost Item
... def report_lost():
...     print("\n--- Report Lost Item ---")
...     name = input("Enter item name: ")
...     desc = input("Enter description: ")
...     location = input("Enter lost location: ")
...     date = input("Enter date: ")
... 
...     item = {
...         "name": name,
...         "desc": desc,
...         "location": location,
...         "date": date
...     }
... 
...     lost_items.append(item)
...     print("Lost item added successfully!\n")
... 
... 
... # Report Found Item
... def report_found():
...     print("\n--- Report Found Item ---")
...     name = input("Enter item name: ")
...     desc = input("Enter description: ")
...     location = input("Enter found location: ")
...     date = input("Enter date: ")
... 
...     item = {
...         "name": name,
...         "desc": desc,
...         "location": location,
...         "date": date
...     }
... 
...     found_items.append(item)
...     print("Found item added successfully!\n")
... 
... 
... # Search Items
... def search_item():
...     print("\n--- Search Item ---")
    keyword = input("Enter item name: ").lower()

    print("\nLost Items:")
    found_flag = False
    for item in lost_items:
        if keyword in item["name"].lower():
            print(item)
            found_flag = True

    print("\nFound Items:")
    for item in found_items:
        if keyword in item["name"].lower():
            print(item)
            found_flag = True

    if not found_flag:
        print("No items found.\n")


# View All Items
def view_all():
    print("\n--- All Lost Items ---")
    if not lost_items:
        print("No lost items")
    else:
        for item in lost_items:
            print(item)

    print("\n--- All Found Items ---")
    if not found_items:
        print("No found items")
    else:
        for item in found_items:
            print(item)


# Match Items
def match_items():
    print("\n--- Matching Items ---")
    match_found = False

    for lost in lost_items:
        for found in found_items:
            if lost["name"].lower() == found["name"].lower():
                print("\nMatch Found!")
                print("Lost Item:", lost)
                print("Found Item:", found)
                match_found = True

    if not match_found:
        print("No matches found.\n")


# Main Menu
while True:
    print("\n====== LIL-CAMP MENU ======")
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. Search Item")
    print("4. View All Items")
    print("5. Match Items")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        report_lost()
    elif choice == "2":
        report_found()
    elif choice == "3":
        search_item()
    elif choice == "4":
        view_all()
    elif choice == "5":
        match_items()
    elif choice == "6":
        print("Thank you for using LIL-CAMP!")
        break
    else:
        print("Invalid choice! Please try again.")
