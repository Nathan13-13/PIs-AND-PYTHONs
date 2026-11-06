def is_palindrome(text):
#Creates a function called is_palindrome that takes a word or sentence.
    text = ''.join(char.lower() for char in text if char.isalnum())
    #char.lower() makes every letter lowercase.      char.isalnum() keeps only letters and numbers, removing spaces and punctuation.      ''.join() puts all the remaining characters together.
    if len(text) <= 1:
        return True
    # If the text has one character or no characters left, it returns True because the word is officially a palindrome.
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])
#