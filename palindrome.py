import string

x = 0
while x != 1:
    phrase = input("Enter a phrase or word to check palindrome: ")
    phrase = phrase.lower()
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace("’", "")
    for v in string.punctuation:
        phrase = phrase.replace(v, "")

    lst = []

    for i in phrase:
        if i in string.punctuation:
            continue
        elif i == "’":
            continue
        else:
            lst.append(i)

    reversed_lst = lst.reverse()
    reversed_word = ''.join(lst)

    if phrase == reversed_word:
        print("A palindrome")
    else:
        print("Not a palindrome")
