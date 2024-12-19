def main():
    names=[]
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            output = "Adieu, adieu, to "
            for name in names:
                index = names.index(name)
                print(index, len(names), name)
                if len(names) == 1:
                    output = output + name
                elif len(names) == 2 and index == 0:
                    output = output + name + " "
                elif index + 1 != len(names):
                    output = output + name + ", "
                else:
                    output = output + "and " + name
            print(output)
            break

main()