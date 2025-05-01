#q1
import random

odd_list = [random.randint(1,100)*2 -1 for _ in range(5)]
    print("list of 5 odd integers:", odd_list)
even_list = [random.randint(1,100)*2 for _ in range(4)]
    print("list of 4 even integers:", even_list)
odd_list[2] = even_list
    print("after replacing the third element:", odd_list)
flattened_list = []
    for item in odd_list:
        if isinstance(item,list):
            flattened_list.extend(item)
        else:
            flattened_list.append(item)
    print("flattened list:", flattened_list)
    flattened_list.sort()
        print("sorted flattened list:", flattened_list)
#q2
        
import random
random_list = [random.randint(1,10) for _ in range(20)]
print("generated list:",random_list)
num = int(input("enter a number to find its positions:"))
    positions = []
        for i in range(len(random_list)):
            if random_list [i] == num:
            positions.append(i)
    print(f"positions of {num} in the list:{positions}")

    
#q3
import random
random_list = [random.randint(1,30) for _ in range (50)]
print("original list:", random_list)
i = 0
while i < len(random_list):
    if random_list.count(random_list[i]) >1:
        random_list.pop(i)
    else:
        i+=1
print("list after removing duplicates:", random_list)


#q4
import random
random_list = [random.randint(-50,50) for _ in range(30)]
print("generated list:", random_list)

positive_list = [num for num in random_list if num >0]
negative_list = [ num for num in random_list if num <0]
print("positive numbers:", positive_list)
print("negative numbers:", negative_list)


#q5
str_list = [ "apple", "banana", "cherry" , "dates", "elderberry"]
print("original list:", str_list)
uppercase_list = [s.upper() for s in str_list]
print("uppercase list:",uppercase_list)


#q6
fahrenheit_list = [32,98.6,212,77,104]
celsius_list = [ (f-32) *5/9 for f in fahrenheit_list]
print(" fahrenheit list:", fahrenheit_list)
print("celsius list:", celsius_list)


#q7
stack = []
while True:
    print("\n menu:")
    print("1. Push")
    print("2. pop")
    print("3. Display stack")
    print("4. exit")
    choice = int (input("enter you choice:"))

    if choice == 1:
        item = input("enter the item to push:")
        stack.append(item)
        print(f"{item} pushed to stack.")
    elif choice == 2:
        if stack:
            print(f" {stack.pop()} popped from stack.")
        else:
            print("stack is empty")
    elif choice == 3:
        print("stack:",stack)
    elif choice == 4:
        break
    else:
        print("invalid choice!")
#q8
queue = []
while True:
    print("\nMenu:")
    print("1. enqueue")
    print("2. dequeue")
    print("3. display queue")
    print("4. exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        item = input("enter the item to enqueue:")
        queue.append(item)
        print(f" {item} added to queue.")
    elif choice == 2:
        if queue:
            print(f" {queue.pop(0)} removed from queue.")
        else:
            print("queue is empty!")
    elif choice == 3:
        print("queue:", queue)
    elif choice == 4:
        break
    else:
        print("invalid choice!")
#q9
lst1 = [1,2,3,4,5,6]
lst2 = [5,6,7,8]
lst3 = [ num for num in lst1 if num not in lst2]
print("list 1:", lst1)
print("list 2:", lst2)
print("list 3:", lst3)
