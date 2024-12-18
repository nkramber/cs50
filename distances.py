distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizone": "58",
    "Pioneer 11": "44 AU"
}


def main():
    spacecraft = input("Enter a spacecraft: ")

    try:
        au = float(distances[spacecraft])
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    except KeyError:
        print(f"Can't find '{spacecraft}'")
        return

    m = convert(au)
    print(f"{m} meters away")


def convert(au):
    return au * 149597870700


main()