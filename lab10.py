#Q-1
import csv
data = [
    ["Name", "Age", "City"],
    ["Alia", 25, "Bhopal"],
]

filename = "people.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerows(data)

print(f"CSV file '{filename}' has been created successfully!")
#Q-1

f = open("C:\\Users\\lab\\Downloads\\people.csv","w")
f.write ("Sandh,")
f.write ("Sharma")
f.write ("87931546164")

f.close()

#Q-2

f = open("C:\\Users\\lab\\Downloads\\people.csv","w")
f.write("Roll no, name,Maths,Physics,Chemistry")
rlno = input("Enter your roll no. [press enter to quit]")
while roll_no:
    nm = input("Enter your name:")
    c,m,p = input("Enter the marks of maths,physics, chemistry").split(" ")
    f.write(rlno + "," +nm+","+c+","+m+","+p+"\n")
    rlno = input("Enter your roll no. [press enter to quit]")
f.close()

#Q-3

f = open("C:\\Users\\lab\\Downloads\\people.csv","a")
f.write("roll no, name, maths,physics,chemistry")
rlno = input("enter your roll no. [press enter to quit]")
while rlno:
    nm = input("enter your name:")
    c,m,p = input("enter the marks of maths,physics, chemistry").split(" " )
    f.write(rlno + "," +nm+","+c+","+m+","+p+"\n")
    rlno = input("enter your roll no. [press enter to quit]")
f.close()

#Q-4

import os    
import shutil  


source_file = "Users\sriva\Downloads\APPLICATIONS_OF_SECOND-ORDER_DIFFERENTIA (1).pdf"  # This is where the file is now


new_folder = 'new'  


if not os.path.exists(new_folder):
    os.mkdir(new_folder)  
    print("New folder created:", new_folder)
else:
    print("Folder already exists:", new_folder)


destination_file = new_folder + "Users\sriva\Downloads\APPLICATIONS_OF_SECOND-ORDER_DIFFERENTIA (1).pdf"

try:
    shutil.copy(source_file, destination_file)
    print("File copied successfully!")
except FileNotFoundError:
    print("The file you're trying to copy does not exist.")
except Exception as error:
    print("Something went wrong:", error)

#Q-5

try:
    with open('source.txt', 'r') as source_file:
        
        content = source_file.read()

        
        content_upper = content.upper()

        
        with open('destination.txt', 'w') as destination_file:
            destination_file.write(content_upper)

        print("File copied successfully with lowercase letters changed to uppercase.")

except FileNotFoundError:
    print("Error: 'source.txt' not found.")
except Exception as e:
    print("An error occurred:", e)

#Q-6

try:
    with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
        
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    
    with open('merged.txt', 'w') as output:
        
        max_len = max(len(lines1), len(lines2))

        
        for i in range(max_len):
            if i < len(lines1):
                output.write(lines1[i].rstrip() + '\n')
            if i < len(lines2):
                output.write(lines2[i].rstrip() + '\n')

    print("Files merged successfully into 'merged.txt'.")

except FileNotFoundError as e:
    print("Error: One of the input files was not found.")
    print(e)
except Exception as e:
    print("An error occurred:", e)

#Q-7

class Employee:
    def _init_(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary

    def display(self):
        print("Employee Code:", self.empcode)
        print("Employee Name:", self.empname)
        print("Date of Joining:", self.date_of_joining)
        print("Salary:", self.salary)


emp = Employee(101, "Alice", "2022-03-15", 55000)


with open("employee.txt", "w") as file:
    file.write(str(emp.empcode) + "\n")
    file.write(emp.empname + "\n")
    file.write(emp.date_of_joining + "\n")
    file.write(str(emp.salary) + "\n")
    print("Employee data saved to 'employee.txt'.")


with open("employee.txt", "r") as file:
    code = int(file.readline().strip())
    name = file.readline().strip()
    joining_date = file.readline().strip()
    salary = float(file.readline().strip())


new_emp = Employee(code, name, joining_date, salary)

print("\nEmployee data read from file:")
new_emp.display()

#Q-8

remove_words = ['a', 'an', 'the']


with open('source.txt', 'r') as infile:
    content = infile.read()


words = content.split()  
filtered_words = [word for word in words if word.lower() not in remove_words]  


cleaned_text = ' '.join(filtered_words)


with open('destination.txt', 'w') as outfile:
    outfile.write(cleaned_text)

print("File processed successfully! Cleaned content saved in 'destination.txt'.")"""
