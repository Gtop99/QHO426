word = input("Enter a word: ")
for letter in word:
    if ord(letter) >= 97 and ord(letter) <= 122:
        print(chr(ord(letter)-32), end = "")
    else:
        print(letter, end = "")
    