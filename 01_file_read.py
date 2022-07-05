import pandas

# # Write file
# def student_data():
#     name = input("Enter your name : ")
#     class_grade = input("Class : ")
#     rollno = input("Roll No. : ")
#     total_marks = input("Total Marks (out of 300): ")

#     return f'Name : {name}\nClass : {class_grade}\nRoll No. : {rollno}\nTotal Marks : {total_marks}/300'

# with open('abc.txt', mode='w') as file:
#     file.write(student_data())


# # Read file
# with open('abc.txt', mode='r') as file:
#     print(file.read())


# # read CSV files
# csv_data = []
# with open('student_data.csv') as file:
#     # csv_data.append(file.readlines(-1))
#     print(pandas.read_csv(file))
