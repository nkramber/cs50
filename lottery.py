import random

def main():
    while True:
        try:
            odds = get_above_zero("What are the odds of winning the lottery?: 1/")
            plays_per_draw = get_above_zero("How many tickets per lottery draw will you buy?: ")
            draws_per_week = get_above_zero("How many times will the lottery draw per week?: ")
            cost_per_ticket = get_above_zero("How much does one ticket cost?: $")
            break
        except (ValueError, IndexError):
            print("Incorrect input! Try again.")
    
    print("\nRunning simulation until you win...")

    tries = 0
    while True:
        tries += 1
        if random.randint(1, odds) == 1:
            money_spent = cost_per_ticket * tries
            time_unit = "weeks"
            time_to_win = int(tries / plays_per_draw / draws_per_week)
            if time_to_win > 52:
                time_unit = "years"
                time_to_win = int(time_to_win / 52)
            
            result = "You beat the odds!"
            if tries > odds:
                result = "You didn't beat the odds..."
                
            print(f"You win! It took you {time_to_win} {time_unit} to win. You spent ${money_spent}. You bought {tries} tickets. {result}")
            break
                
def get_above_zero(s):
    while True:
        try:
            v = round(float(input(s).replace(" ", "")))
            if v <= 0:
                print("Incorrect input! Try again.")
            else:
                return v
        except (ValueError, IndexError):
            print("Incorrect input! Try again.")
            
main()