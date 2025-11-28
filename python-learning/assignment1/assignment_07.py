def palindrome_checker(word):
    if word == word[::-1]:
        return "palindrome"
    else:
        return "not palindrome"
word = input("Enter any string: ")
print(f"the string is {palindrome_checker(word)}");

 


