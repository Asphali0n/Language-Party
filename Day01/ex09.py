sentence = input("Enter a sentence: ")
inverse_sentence = sentence[::-1]

if sentence == inverse_sentence:
    print("It's a palindrome")
else:
    print("It's not a palindrome")