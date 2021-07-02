intro = input("Enter you intro: ")
print(intro)
cCount = 0
wCount = 1
for character in intro:
    cCount = cCount + 1
    if(character == " "):
        wCount = wCount + 1
print("Number of words: ")
print(wCount)
print("Number of characters: ")
print(cCount)
