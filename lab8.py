#8.1
def set1():
    sentence = input("enter the sentence: ").split()
    print (sentence)
    s = set()
    s = {x.upper() for x in sentence}
    print(s)
set1()

#8.2
import random
def set2():
    s = set()
    while len(s) != 10:
        x = random.randint(15,45)
        s.add(x)
    print(s)
    d = set()
    c = 0
    for x in s:
        if x < 30:
            c += 1
        if x > 35:
            d.add(x)
    s = s - d
    print("No. of elements<30 ", c)
    print("After deleting all the values>35" , s)

set2()


#8.3
def set3():
    s = set()
    for i in range(5):
        s.add(input("Enter a name: "))
    print(s)
    nm = input("enter a name to modify: ")
    if nm in s:
        newnm = input("replace it with: ")
        s.pop(nm)
        s.add(newnm)
    else:
        print(nm,"not found")
    print(s.popitem(), " is deleted ")
    print(s.popitem(), " is deleted ")
    print("The final list: ", s)
    
set3()


#8.4
def set4():
    s = {'vidhi' , 'naiyya' , 'swaroopa' , 'vruti' , 'krissa'}
    sa = set()
    sb = set()
    for nm in s:
        if nm[0] == 'a':
            sa.add(nm)
        elif nm[0] == 'b':
            sb.add(nm)
    sa1 = {nm for nm in s if nm[0] == 'a'}
    print(sa)
    print(sb)#8.1
def set1():
    sentence = input("enter the sentence: ").split()
    print (sentence)
    s = set()
    s = {x.upper() for x in sentence}
    print(s)
set1()

