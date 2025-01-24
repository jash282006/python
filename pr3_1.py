string1=str(input('writ your string'))

vow='aeiouAEIOU'
count=0
for  char in string1:
    if char in vow:
     count+=1
print('no of vowel is ',count)
