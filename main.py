
# ID     Name   Age
# field1\tfield2\tfield3\n
# field1\tfield2\tfield3\n

from student import student
from teacher import teacher
from admin import admin

def main():
    choice = 1
    while choice != 0:
        print('1- Student')
        print('2- Teacher')
        print('3- Admin')
        print('0- Exist\n')
        choice = int(input('Choice: '))
        if choice == 1:
            student()
        elif choice == 2:
            teacher()
        elif choice == 3:
            admin()
        elif choice != 0:
            # choice not in [0 ... 3]
            print('Choose a number between 0 and 3')

    print('--> Goodbye <--')

if __name__ == "__main__":
    main()