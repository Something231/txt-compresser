import json
with open('input.txt') as f:
    lines = f.read()

lines = lines.replace("0", "$0")
lines = lines.replace("1", "$1")
lines = lines.replace("2", "$2")
lines = lines.replace("3", "$3")
lines = lines.replace("4", "$4")
lines = lines.replace("5", "$5")
lines = lines.replace("6", "$6")
lines = lines.replace("7", "$7")
lines = lines.replace("8", "$8")
lines = lines.replace("9", "$9")

words = lines.split()
freg = ""

with open("wordlist.json", 'r') as json_file:
    dic = json.load(json_file)

for word in words:
    if word in dic:
        uwu = dic[word]
        freg = f"{freg}{uwu}+"
    else:
        freg = f"{freg}{word}+"

with open("output.txt", 'w') as text_file:
    text_file.write(freg)

print("Compression Done!")