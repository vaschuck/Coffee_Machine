def reverse_word(word):
    reverse = ''
    for letter in word:
        reverse = letter + reverse
    return reverse


def is_palindrome(word):
    return word == reverse_word(word)


letters = input()

print('Palindrome' if is_palindrome(letters) else 'Not palindrome')
