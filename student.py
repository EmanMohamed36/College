from help import *

def write_student():
    c = 'y'
    with open('Student.txt', 'a') as student_file:
        while c.lower() == 'y':
            student_id = input("What's your id?\n>>")
            student_name = input("What's your name?\n>>")
            student_age = input('How old are you?\n>>')
            student_file.write(student_id + '\t' + student_name + '\t' + student_age + '\n')
            c = input('Do you want to enter another record (y / n) ? ')
        print('File saved successfully')

def read_student():
    with open('Student.txt', 'r') as student_file:
        print('ID\tName\tAge')
        print('-------------------')
        for record in student_file:
            print(record, end='')

def search_student():
    student_id = input('Enter the id of the student to search for: ')
    with open('Student.txt', 'r') as student_file:
        flag = False
        for record in student_file:
            fields = record.split('\t')
            if student_id == fields[0]:
                flag = True
                print('ID\tName\tAge')
                print('-------------------')
                print(record)
                break
        if not flag:
            print('Student not found')

def delete_student():
    student_id = input('Enter the id of the student to delete: ')
    with open('Student.txt', 'r') as student_file, open('Temp.txt', 'w') as temp_file:
        flag = False
        for record in student_file:
            fields = record.split('\t')
            if student_id == fields[0]:
                flag = True    
            else:
                temp_file.write(record)
        if not flag:
            print('Student not found')
        else:
            print('Student deleted successfully')
    os.remove('Student.txt')
    os.rename('Temp.txt', 'Student.txt')

def update_student():
    student_id = input('Enter the id of the student to update: ')
    with open('Student.txt', 'r') as student_file, open('Temp.txt', 'w') as temp_file:
        flag = False
        for record in student_file:
            fields = record.split('\t')
            if student_id == fields[0]:
                flag = True    
                student_age = input("Enter the new age for " + fields[1] + "?\n>>")
                record = student_id + '\t' + fields[1] + '\t' + student_age + '\n'
            temp_file.write(record)
        if not flag:
            print('Student not found')
        else:
            print('Student updated successfully')
    os.remove('Student.txt')
    os.rename('Temp.txt', 'Student.txt')


def student():
    1

