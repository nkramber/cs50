entrees = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    get_order()
    
    
def get_order():
    total_price = round(0, 2)
    while True:
        try:
            item = input("Item: ")
            item = item.title()
            if item in entrees:
                total_price += entrees[item]
                print(f"Total: ${total_price:.2f}", sep="")
            else:
                continue
        except EOFError:
            print("/n")
            break
        
    
main()