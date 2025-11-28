def vowel_counter(word):
    count = 0
    for i in word:
      if i =='a' or i =='e' or i =='i' or i =='o' or i =='u':
            count = count + 1
    return count

word = input("Enter a string: ")
print('The number of vowels in the string is: %d' %(vowel_counter(word)))