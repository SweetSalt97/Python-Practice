msg = input (">")
wrd =msg.split(" ")
#Uses the given object to make boundaries from given and make a list
print(wrd)

emojis = {
    ":)": "😊",
    ":(": "☹️"
}
output =""
for word in wrd:
    output += emojis.get(word, word) + " "
print(output)