s = input("Enter a word ")
k=0
b={'a','e','i','o','u'}
l=s.lower()
for i in l:
    if i in b:
        k=k+1
print(k)



c = 0
j=0
for i in range(0, len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
        c = c+1

    else:
        j=j+1
print("no of vowels are ->",c)
print("no of consonants are ->",j)
