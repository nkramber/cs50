def main():
    print(get_percent())
        

def get_percent():
    while True:
        fuel_level = input("Input fuel level as a fraction: ").split("/")
        if len(fuel_level) != 2:
            continue
        try:
            for i in range(len(fuel_level)):
                fuel_level[i] = int(fuel_level[i])
            percent = int(fuel_level[0] / fuel_level[1] * 100)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        if percent > 100:
            continue
        if percent == 0 or percent == 1:
            percent = "E"
        elif percent == 99 or percent == 100:
            percent = "F"
        else:
            percent = str(percent) + "%"
        return percent

main()