def is_palindrome(string):
    return(string[::-1] == string)

word_to_check = 'abccba'
print("Word to check if palindrome:", word_to_check)
print(is_palindrome(string = word_to_check))
