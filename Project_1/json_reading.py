import json
data = json.load(open("data.json"))
user_input = input("Enter a word: ")
print(data[user_input])
