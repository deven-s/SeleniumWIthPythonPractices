import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 1:
        print("did you mean %s instead" % get_close_matches(word, data.keys())[0])
        decide = input("press Y for yes or N for no")
        if decide.upper() == "Y":
            return data[get_close_matches(word, data.keys())[1]]
        elif decide.upper() == "N":
            return "pugger your paw steps on wrong keys"
        else:
            return "you have entered wrong choice, please enter Y or N"
    else:
        print("The word doesn't exist in the dictionary, Try different word")


word = input("Enter the word you want to search: ")

output = translate(word)
# print(output)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
