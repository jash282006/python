
#Q1
names_list=[("b1",),("b2",),"g1","g2","g3",("b3",),"g4",("b4",)]
boy_count=sum(1 for name in names_list if isinstance(name,tuple))
girl_count=sum(1 for name in names_list if isinstance(name,str))

print("Number of boys:",{boy_count})
print("Number of girls:",{girl_count})
    

#Q2
students=[(101,"Vidhi",19),\
          (103,"Swaroopa",20),\
          (102,"Naiyya",26),\
          (104,"Dharm",27),\
          (105,"Haard",21)]
roll_number=[]
names=[]
ages=[]

for student in students:
    roll_number.append(student[0])
    names.append(student[1])
    ages.append(student[2])

print("Roll number of the student:",roll_number)
print("Name of the student :",names)
print("age of the student :",ages)


#Q3
import datetime
def dates():
    d1=(18,2,2025)
    d2=(18,2,2024)
    date1=datetime.date(d1[2],d1[1],d1[0])
    date2=datetime.date(d2[2],d2[1],d2[0])
    print(type(date1))
    print(abs(date1-date2))

dates()



#Q4
def food():
    
    food_items=[('Panner tikka',99),('Hakka noodles',109),('Veg Sandwich',119),('Panner chilli',149)]
    for x in food_items:
        print(x)
    print(sorted(food_items))
    import operator
    print(sorted(food_items,key=operator.itemgetter(1),reverse= True))
food()



#Q5
tuple_list=[(),(1,2),(),(3,4),("hello",),()]
filtered_list=[t for t in tuple_list if t ]
print("List after removing the empty tuple:",filtered_list)

#Q6
def modifiy_element_of_tuple():
    t1=('A','B','C','D')
    t1_list=list(t1)
    t1_list[2]='V'
    t2=tuple(t1_list)
    print(t2)
modifiy_element_of_tuple()


#Q7
my_tuple=(1,2,3,4,5,6,7,8)
l=list(my_tuple)
l.pop(2)
print(l)
a=tuple(l)





















