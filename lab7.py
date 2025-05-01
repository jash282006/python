#7.1
d1 = {'a': 1}
d2 = {'b': 2}
d3 = {'c': 3}


d4 = {}
d4.update(d1)
d4.update(d2)
d4.update(d3)


print("Combined Dictionary:", d4)

#7.2
def empty_or_not(d):
    if not d:
        print("The dictionary is empty.")
    else:
        print("The dictionary is not empty.")

d1={}
d2={'a':18,'v':4}
empty_or_not(d1)
empty_or_not(d2)

#7.3
dept_salaries = {
    101: [50000, 60000, 55000],
    102: [45000, 47000],
    103: [70000, 72000, 68000]
}


for dept, salaries in dept_salaries.items():
    print(f"Department {dept}: \n Min Salary: {min(salaries)}, Max Salary: {max(salaries)}")

#7.4

text = input("Enter a string: ")


char_freq = {}

for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("Character frequencies:", char_freq)




