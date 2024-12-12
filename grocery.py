def main():
    grocery_list = get_grocery_list()
    for grocery in grocery_list:
        print(grocery_list[grocery], grocery)
    
    
def get_grocery_list():
    grocery_list = {}
    while True:
        try:
            grocery = input("Grocery to add to list: ")
            grocery = grocery.upper()
            if grocery in grocery_list:
                grocery_list[grocery] = grocery_list[grocery] + 1
            else:
                grocery_list[grocery] = 1
        except EOFError:
            print("")
            return dict(sorted(grocery_list.items()))

main()