#To display emojis on windows, you press win + . (period)
message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word)+ " "
    print(output)