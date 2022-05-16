from help import *
from student import *

def searchStudent():
    stu_id = input('Enter the ID of the student to search for:')
    flag = 0
    with open('Student.txt','r') as file:
        for line in file:
            fields = line.split('\t')
            if stu_id == fields[0]:
                print(line,end = '')
                flag = 1
        if not flag:
            print('Not Found')

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
    if flag:
        with open('Teachers.txt', 'r') as teacher_file, open('Temporary.txt', 'w') as temporary_file:
            flag = False
            for record in teacher_file:
                fields = record.split('\t')
                if student_id not in fields[5:]:
                    temporary_file.write(record)

        os.remove('Teachers.txt')
        os.rename('Temporary.txt', 'Teachers.txt')


def ctrl_student():
    while 1:
        print('Admin Page (Control Student)')
        print('choose: ')
        print('1- Show All Student ')
        print('2- Search Student ')
        print('3- Add ')
        print('4- Remove ')
        print('5- Edit ')
        print('6- Return ')
        Ad_Stud_choice = input('Choise: ')
        if Ad_Stud_choice == '1':
            #show all student
            read_student()
            Directing()
        elif Ad_Stud_choice == '2':
            #search student
            searchStudent()
            Directing()
        elif Ad_Stud_choice == '3':
            #Add
            write_student()
            Directing()
        elif Ad_Stud_choice == '4':
            #remove
            delete_student()
            Directing()
        elif Ad_Stud_choice == '5':
            #Edit
            update_student()
            Directing()
        elif Ad_Stud_choice == '6':
            #return
            Returning()
            return
                                
