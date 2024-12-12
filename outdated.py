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

def main():
    y, m, d = get_date()
    print(y + "-" + m + "-" + d)
    
    
def get_date():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                m, d, y = date.split("/")
                if (int(m) < 1 or int(m) > 12):
                    continue
                if (int(d) < 1 or int(d) > 31):
                    continue
                if (int(y) < 0):
                    continue
                return(y, m, d)
            m = date.split(" ")[0].capitalize()
            if m in months:
                d = date.rsplit(",")[0] #Make it not work if no comma
                print (d) #Continue defining what a valid date is, get the day split from the month
        except ValueError:
            pass
    
    
main()