# I was driving on the highway the other day and I happened to notice my odometer. Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.
# “Now, what I saw that day was very interesting. I noticed that the last 4 digits were palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.
# “One mile later, the last 5 numbers were palindromic. For example, it could have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And you ready for this? One mile later, all 6 were palindromic!
# “The question is, what was on the odometer when I first looked?”

def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1
    return True

def is_correct(i):
    str_i = str(i)
    if len(str_i) >= 6:
        # Check the last 4 digits
        if is_palindrome(word = str_i[-4:len(str_i)]):
            # Check the last 5 digits
            str_ii = str(i + 1)
            if is_palindrome(word=str_ii[-5:len(str_ii)]):
                # Check the middle 4 digits
                str_iii = str(i + 2)
                if is_palindrome(word=str_iii[-5:(len(str_iii)-1)]):
                    # Check all 6
                    str_iv = str(i + 3)
                    if is_palindrome(str_iv):
                        print("Last four:", str_i)
                        print("Last five:", str_ii)
                        print("Middle four:", str_iii)
                        print("All six:", str_iv)
                        return True

    return False

for i in range(1000000):
    if is_correct(i):
        print(i)

print("\nAll done:)")

