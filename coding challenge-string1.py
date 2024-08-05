str = input("Enter a string : ")
str = str.lower()
len = len(str)
vowel = 0
consonant = 0
for ch in str:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        vowel += 1
    else:
        consonant += 1
print("The number of vowels in the string : ",vowel)
print("The number of consonants in the string : ",consonant)
