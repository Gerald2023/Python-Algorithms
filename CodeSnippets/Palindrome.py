# start of function

def reverse(word):
    length = len(word)
    reversed_word = ""

    for a in range(length, 0, -1):
        a -= 1

        reversed_word = reversed_word + word[a]

        # print(word[a])
    if reversed_word == word:
        print(f'Your word "{word}" is Palindrome')
    else:
        print(f'Your word "{word}" is NOT Palindrome')


# end of function
reverse("madam")
