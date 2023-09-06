import json
with open('compressed.txt') as f:
    text = f.read()

words = text.split("+")
decompressed = ""

with open("wordlist.json", 'r') as json_file:
    dic = json.load(json_file)

for word in words:
    if any(char in word for char in "0123456789"):
        if word.startswith('$') == True:
            decompressed = f"{decompressed}{word} "
        elif word.isdigit():
            key_list = list(dic.keys())
            val_list = list(dic.values())
            word = int(word)
            position = val_list.index(word)
            word = key_list[position]
            decompressed = f"{decompressed}{word} "
        elif word.startswith("#") == True:
            word = word.replace("#", "")
            word = int(word)
            for child in range(word):
                decompressed = f"{decompressed} "
        elif "$" in word:
            wordz = word.split("$")
            decompressed = f"{decompressed}{wordz[0]} {wordz[1]} "
        else:
            decompressed = f"{decompressed}error "
    else:
        decompressed = f"{decompressed}{word} "

decompressed = decompressed.replace("$0", "0")
decompressed = decompressed.replace("$1", "1")
decompressed = decompressed.replace("$2", "2")
decompressed = decompressed.replace("$3", "3")
decompressed = decompressed.replace("$4", "4")
decompressed = decompressed.replace("$5", "5")
decompressed = decompressed.replace("$6", "6")
decompressed = decompressed.replace("$7", "7")
decompressed = decompressed.replace("$8", "8")
decompressed = decompressed.replace("$9", "9")


with open("decompressed.txt", 'w') as text_file:
    text_file.write(decompressed)

print("Decompression Done!")
