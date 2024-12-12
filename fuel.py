def main():
    print(get_percent())
        

def get_percent():
    while True:
        try:
            x, y = input("Input fuel level as a fraction: ").split("/")
            x = int(x)
            y = int(y)
            fuel = int(x / y * 100)
            if fuel < 99 and fuel > 1:
                return str(fuel) + "%"
            if fuel == 0 or fuel == 1:
                return "E"
            if fuel == 99 or fuel == 100:
                return "F"
        except (ValueError, ZeroDivisionError):
            pass


main()