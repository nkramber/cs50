import requests
import json

def main():
    user_input = input("Enter search category(song, artist, or album), search term, and quantity of results desired separated by a comma: \n")
    category, term, quantity = user_input.split(", ")
    make_lowercase(category)
    make_lowercase(term)
    make_lowercase(quantity)
    if category == "artist":
        category = ""
    else:
        category = "entity=" + category + "&"
        
    url = f"https://itunes.apple.com/search?{category}limit={quantity}&term={term}"
    results = requests.get(url).json()
    formatted_results = json.dumps(results, indent=2)
    
    error_number = 0
    
    for result in results["results"]:
        try:
            print("Song: " + result["trackName"] + ", Artist: " + result["artistName"])
        except KeyError:
            print("Search error", error_number)
            error_number += 1

def make_lowercase(s):
    return s.lower()

main()