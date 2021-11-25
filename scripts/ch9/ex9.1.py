# Write a program that reads and prints only the words with more than 20 characters (not counting whitespace).
fin = open(file = "scripts/ch9/words.txt")

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)







