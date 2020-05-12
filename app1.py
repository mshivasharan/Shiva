import json
import difflib

data = json.load(open("data.json"))

#Display final format of meaning from the dictionary 
def display_format(word, data):
    output = ''
    for i in range(len(data[word])):
        output += str(i+1) + '. ' + str(data[word][i]) + '\n'
    return output

#finds closer match using difflib library
def closermatcher(word, data):
    closermatch = difflib.get_close_matches(word, data.keys())
    if len(closermatch) > 0:
        opinion = input("Did you mean %s, if yes press Y, if no press N: " % closermatch[0])
        if opinion.lower() == 'y':
            return display_format(closermatch[0], data)
        elif opinion.lower() == 'n': 
            return "The word doesn't exists, please double check it"
    else:
        return "we did not understand your entry"

#finds meanings for a word
def meaning(word):
    word = word.lower()
    #if check word in data else call closematcher
    if word in data:
        return display_format(word, data)
    elif word.title() in data:
        return display_format(word.title(), data)
    elif word.upper() in data:
        return display_format(word.upper(), data)
    else:
        return closermatcher(word, data)

#main program
if __name__ == "__main__":
    word = input("Enter a word: ")
    print(meaning(word))