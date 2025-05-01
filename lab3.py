'''#Cp1
word=input("Enter a string:")
count =0
vow="AEIOUaeiou"
for char in word:
    if char in vow:
        count +=1
print("Number of vowels",count)



#CP2

def lower(s):
    result=""
    for char in s:
        if 'A' <=char<='Z':
            result += chr(ord(char)+32)
        else:
            result+=char
    return result
    
def upper(s):
    result=""
    for char in s:
        if 'a' <=char<='z':
            result += chr(ord(char)-32)
        else:
            result+=char
    return result

def toggle(s):
    result=""
    for char in s:
        if 'a' <=char<='z':
            result += chr(ord(char)-32)
        elif 'A' <=char<='Z':
            result += chr(ord(char)+32)
        else:
            result+=char
    return result
s=input("Enter a string: ")
    
print("original word",s)
print("Lowercase word",lower(s))
print("Upper word",upper(s))
print("Toggle word",toggle(s))


'''
#CP3
s1=input("Enter a string 1:")
s2=input("Enter a string 2:")

found= False
len1,len2 =len(s1),len(s2)

for i in range (len1-len2+1):
    if s1[i:i+len2]==s2:
        found= True
        break
    if found:
        print({s2},"is present in",{s1})
    else:
        print({s2},"is not present in",{s1})


#CP 4














