s = str(input("Please enter a word: "))
print("Total vowel found: ", end='')
count = 0
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        count += 1
print(count)
print("Total consonant found: ", end='')
count = 0
for i in range(len(s)):
    if s[i] not in 'aeiouAEIOU':
        count += 1
print(count)