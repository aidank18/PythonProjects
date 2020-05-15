f = open("test.txt")

for word in f:
    for letter in word:
        print(letter)
f.close()
f = open("test.txt")
for line in f:
    for word in line.split():
        print(word)
