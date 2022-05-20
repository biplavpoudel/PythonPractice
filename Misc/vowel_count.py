str = "Hello World"
count = 0
vowel = ['a', 'e', 'i', 'o', 'u']
for c in str:
     if c in vowel:
    #  if ( c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        count = count + 1
print (count)
print("Number of vowels= %d"%count)