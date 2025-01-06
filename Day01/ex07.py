vowels = ["a","e","i","o","u"]
sentence = input("Enter a sentence: ")
nb_vowels = 0

for letter in sentence:
    if letter.lower() in vowels:
        nb_vowels += 1

print(nb_vowels)


