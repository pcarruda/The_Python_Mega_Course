#library import
import json
from difflib import get_close_matches

#data aquisition
data = json.load(open("data.json"))

#function define
def translate(w):

    w = w.lower() #Force the user to imput a lower case letter for word definitions
    if w in data:
        return data[w]
    elif w.title() in data: #bug correction to understand proper nouns like Paris or Dekhi
        return data[w.title()]
    elif w.upper() in data: #another bug correction to understand acronyms like USA ou NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn1 = input("Did you mean %s instead? Enter Y for yes or N for no: " %get_close_matches(w, data.keys())[0])
        yn1 = yn1.upper()
        if yn1 == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn1 == "N" and get_close_matches(w, data.keys())[1]:
            yn2 = input("Did you mean %s instead? Enter Y for yes or N for no: " %get_close_matches(w, data.keys())[1])
            yn2 = yn2.upper()
            if yn2 == "Y":
                return data[get_close_matches(w, data.keys())[1]]
            elif yn2 == "N":
                return "The input word doesn't exist. Please enter another word."
            else:
                return "Can't understand your entry. Please press Y for yes or N for no."
        else:
            return "Can't understand your entry. Please press Y for yes or N for no."
    else:
        return "The word doesn't exist. Please enter again!"

#user interface
user_input = input("Enter a word: ")
output = translate(user_input)
if type(output) == list: #a more user friendly response
    for item in output:
        print(item)
else:
    print(output)
