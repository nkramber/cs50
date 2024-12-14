months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

errors = []

def main():
    print("This program converts dates from American formatting to international standard formatting (YYYY-MM-DD")
    y, m, d = get_date()
    print(y, m, d, sep="-")
    
    
def get_date():
    while True:
        try:
            print("Enter a date in the format 'MM/DD/YYYY' or 'name of month DD, YYYY': ")
            date = input()
            if date == "":
                print("Please enter a date")
                continue
            if "/" in date:
                try_again = False
                m, d, y = date.split("/")
                if int(m) < 1 or int(m) > 12:
                    print("Invalid date")
                    try_again = True
                if int(d) < 1 or int(d) > 31:
                    print("Invalid date")
                    try_again = True
                if int(y) < 1000 or int(y) > 2025:
                    print("Invalid date")
                    try_again = True
                if try_again:
                    continue
                return y, m, d
            else:
                m, d, y = date.split(" ")
                m = m.capitalize()
                if m in months:
                    m = months.index(m) + 1
                    if "," in d:
                        d = d.replace(",", "")
                        if int(d) <= 31 and int(d) >= 1:
                            if int(y) <= 2025 and int(y) >= 1000:
                                return y, m, d
                            else:
                                print("Invalid date")
                        else:
                            print("Invalid date")
                    else:
                        print("Invalid date")
                else:
                    print("Invalid date")
        except ValueError:
            pass
    
    
main()