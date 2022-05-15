from help import *

def write_student():    #Done
    with open('Student.txt', 'a') as student_file:
        Name = input("Name: ")
        Age = input("Age: ")
        Department = input("Department: ")
        Level = input("Level: ")
        Password = str(getpass("Password: "))
        Id = str(students_ids.get())
        this_stu = Id + '\t' + Name + '\t' + Age + '\t' + Department + '\t' + Level + '\t' + Password + '\t\n'
        student_file.write(this_stu)
        print("\nRegistration Completed ... Your ID is: ", Id)
    return this_stu.split('\t')

def read_student():
    with open('Student.txt', 'r') as student_file:
        print('ID\tName\tAge\tDepartment\tLevel\tPassword')
        print('------------------------------------------')
        for record in student_file:
            print(record, end='')
        print('\n')

def search_student(_id = '-1', _password = '-1'):
    with open('Student.txt', 'r') as student_file:
        for record in student_file:
            fields = record.split('\t')
            if _id == fields[0] and fields[5] == _password:
                return [True, fields]
    return [False, []]

# def delete_student():
#     student_id = input('Enter the id of the student to delete: ')
#     with open('Student.txt', 'r') as student_file, open('Temp.txt', 'w') as temp_file:
#         flag = False
#         for record in student_file:
#             fields = record.split('\t')
#             if student_id == fields[0]:
#                 flag = True    
#             else:
#                 temp_file.write(record)
#         if not flag:
#             print('Student not found')
#         else:
#             print('Student deleted successfully')
#     os.remove('Student.txt')
#     os.rename('Temp.txt', 'Student.txt')

def add_new_course(_id = '-1', course_id = 'none'):
    with open('Student.txt', 'r') as student_file, open('Temp.txt', 'w') as temp_file:
        flag = False
        for record in student_file:
            fields = record.split('\t')
            fields.pop()
            if _id == fields[0]:
                flag = True
                fields.append(course_id)
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
                this_student = record.split('\t')
            temp_file.write(record)
        if not flag:
            print('Student not found')
        else:
            print('Student updated successfully')
    os.remove('Student.txt')
    os.rename('Temp.txt', 'Student.txt')
    return this_student

def update_student(_id = '-1'):
    with open('Student.txt', 'r') as student_file, open('Temp.txt', 'w') as temp_file:
        flag = False
        for record in student_file:
            fields = record.split('\t')
            fields.pop()
            if _id == fields[0]:
                flag = True    
                fields[5] = getpass("Enter the new password for " + fields[1] + ": ")
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
                this_student = record.split('\t')
            temp_file.write(record)
        if not flag:
            print('Student not found')
        else:
            print('Student updated successfully')
    os.remove('Student.txt')
    os.rename('Temp.txt', 'Student.txt')
    return this_student

def student():
    Directing()
    this_student = []
    choice = '1'
    while choice != '0':
        print("1- Register")
        print("2- Sign in")
        print("0- Return Back")
        choice = input('Choose: ')
        
        if choice == '0':
            Returning()
            return 
        
        found = 0
        Directing()

        if choice == '1':
            # Register 
            found  = 1
            print("Student Register Page")
            this_student = write_student()

        elif choice == '2':
            # sign in 
            print("Student Sign In Page")
            student_id = input('Enter ID: ')
            student_pass = getpass('Enter Password: ')
            [found, this_student] = search_student(student_id, student_pass)

        if not found:
            print("The ID or the Password is wrong, Please try Aagin")
            press_any()
            Returning()
            return


        stu_choic = '1'
        while stu_choic != '0':
            Directing()
            print('1- Show my Info')
            print('2- Add a new course')
            print('3- Show my courses')
            print('4- Update password')
            print('0- Logout')
            stu_choic = input('Choose: ')
            if stu_choic == '0':
                Returning()
                return
            
            Directing()

            if stu_choic == '1':
                print('ID\tName\tAge\tDepartment\tLevel\tPassword')
                print('------------------------------------------')
                for i in range(6):
                    print(this_student[i] + '\t', end='')
                print()
                press_any()
            elif stu_choic == '2':
                # Add new course
                courses_found = 0
                with open('Teachers.txt', 'r') as teacher_file:
                    for record in teacher_file:
                        fields = record.split('\t')
                        if fields[0] not in this_student[6:]:
                            print(fields[0] + '- ' + fields[3])
                            courses_found += 1
                    if courses_found > 0:
                        course_choice = input('Choose: ')
                        this_student = add_new_course(this_student[0], course_choice)
                    else:
                        print("There is no available courses for you now!")
                        press_any()
            elif stu_choic == '3':
                # show my courses
                with open('Teachers.txt', 'r') as teacher_file:
                    for record in teacher_file:
                        fields = record.split('\t')
                        if fields[0] in this_student[6:]:
                            print(fields[0] + '- ' + fields[3])
                press_any()
                
            elif stu_choic == '4':
                this_student = update_student(this_student[0])
